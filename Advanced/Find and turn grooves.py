"""
EN: A program that looks for grooves in a file. Since the client's tool can only move along the X axis, we need to automatically rotate the part while checking for exclusions (for example, perpendicular lines).
DE: Ein Programm, das nach Rillen in einer Datei sucht. Da das Werkzeug eines Kunden nur entlang der X-Achse bewegt werden kann, müssen wir das Detail automatisch drehen, während wir Ausschlüsse überprüfen (zum Beispiel senkrechte Linien).
"""

from datetime import datetime
from company import gdb
from company import dlg
from company.gdb import cad, path
from company.gdb.view import redraw_window, zoom_all
from config import run_config
from sclcore import do_debug


def main():
    do_debug()
    counter_of_turns = 0 #create bool if i turned, to compare if i turn more than 1 time within 1 part
    parts = gdb.get_entities()
    for part in parts:
        layers = gdb.get_entities(part)
        for layer in layers:
            layer_name = layer.split("\\")
            layer_name = layer_name[-1]

            if layer_name.upper().startswith("NUTX"):
                NutX_lines = gdb.get_entities(layer) #list of single lines (geometries)
                NutX_paths_count = path.reorder(layer) #(int) number of detected paths
                if len(NutX_lines) == NutX_paths_count: #if single lines (geometries) == paths  => no closed geometries
                    check_opened_geom(NutX_lines, part)

                elif len(NutX_lines) > NutX_paths_count: #if theres a closed geometry
                    check_closed_geom(NutX_paths_count, part, layer_name, layer)
        if counter_of_turns > 1:
                        dlg.output_box(f"Nuten sind nicht parallel. Das Teil {part} an der Linie {NutX_lines[j]} ausgerichtet.")


def is_horisontal(NutX_line): #if start and end lines are on the same y level they're horisontal
    start_nutx_line = gdb.get_start_point(NutX_line) #vec3 x y z
    end_nutx_line = gdb.get_end_point(NutX_line)
    return start_nutx_line.y == end_nutx_line.y 


def is_vertical(NutX_line): #if start and end lines are on the same y level they're horisontal
    start_nutx_line = gdb.get_start_point(NutX_line) #vec3 x y z
    end_nutx_line = gdb.get_end_point(NutX_line)
    return start_nutx_line.x == end_nutx_line.x 


def turn(part, NutX_line):
    angle_to_turn = gdb.get_angle(NutX_line)
    cad.rotate_piece(part, 0, 0, -angle_to_turn, create_copy=False)
    gdb.set_note(part, 'NRAN', '0')


def check_if_rectangle(new_layer):
    straight_lines = []
    lines = gdb.get_entities(new_layer)
    if len(lines) == 4:
        for line in lines: # i can just take odd lines
            if is_horisontal(line) or is_vertical(line):
                straight_lines.append(line) #can delete that from list to not clutter up the memory
        if len(straight_lines) == 4:
            return True
        else: #lines are not straight
            dlg.output_box(f"Eine oder mehrere Linien sind nicht gerade, bitte überprüfen Sie die Figur.")

    else: #not 4 lines
        dlg.output_box(f"Es sollten 4 Linien in der Figur sein, aber es sind nicht 4. Bitte überprüfen Sie die Figur.")
    return False


def check_opened_geom(NutX_lines, part):
    for j in range (NutX_lines):
        if not is_horisontal(NutX_lines[j]):
            turn(part, NutX_lines[j])
            counter_of_turns += 1


def check_closed_geom(NutX_paths_count, part, layer_name, layer):
    closed_geoms = []
    new_layers = []
    for i in range(NutX_paths_count):
        new_layer = gdb.add_layer(part, f"{layer_name}_new_layer_{i+1}") #do i need to add part?
        path.extract(layer, i+1, new_layer, erase_source_object = True)
        new_layers.append(new_layer)

        if path.is_closed(new_layer):
            closed_geoms.append(new_layer)
            NutX_new_lines = gdb.get_entities(new_layer)
            counter = 1

            for NutX_new_line in NutX_new_lines:
                if counter == 1:
                    longest_line = NutX_new_line
                    length = gdb.get_length(NutX_new_line)
                    counter += 1
                else:
                    if length < gdb.get_length(NutX_new_line):
                        length = gdb.get_length(NutX_new_line)
                        longest_line = NutX_new_line

            if not is_horisontal(longest_line):
                turn(part, longest_line)
                counter_of_turns += 1
                do_debug()
                if not check_if_rectangle(new_layer):
                    dlg.output_box(f"Kann mit dieser Figur nicht fortfahren. Sie sollten es entweder manuell einrichten oder den Support kontaktieren.")



if __name__ == '__main__':
    main()
