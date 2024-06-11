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
    parts = gdb.get_entities()
    for part in parts:
        layers = gdb.get_entities(part)
        for layer in layers:
            layer_name = layer.split("\\")
            layer_name = layer_name[-1]

            if layer_name.upper().startswith("NUTX"):
                counter_of_turns = 0 
                NutX_lines = gdb.get_entities(layer) #list of single lines (geometries)
                NutX_paths_count = path.reorder(layer)
                if len(NutX_lines) == NutX_paths_count: #if single lines (geometries) == paths   it means: no closed geometries
                    counter_of_turns = check_opened_geom(NutX_lines, part, counter_of_turns)

                elif len(NutX_lines) > NutX_paths_count:
                    counter_of_turns = check_closed_geom(NutX_paths_count, part, layer_name, layer, counter_of_turns)
                if counter_of_turns > 1:
                        dlg.output_box(f"Nuten sind nicht parallel. Das Teil '{part}' ist falsch.")


def check_opened_geom(NutX_lines, part, counter_of_turns):
    """
    Check each line, turn the part with this line horisontal if it's not already.

    :param NutX_lines: list of lines (by default expecting Nut(groove))
    :type NutX_lines: list
    :param part: part that will be turned according to a reference line
    :type part: str
    :param counter_of_turns: counter for how many times the part was turned, to catch cases where the part has non-parallel lines
    :type counter_of_turns: int
    :return: updated counter_of_turns
    :rtype: int
    """

    for j in range(len(NutX_lines)):
        if not is_horisontal(NutX_lines[j]):
            turn(part, NutX_lines[j])
            counter_of_turns += 1
    return counter_of_turns


def check_closed_geom(NutX_paths_count, part, layer_name, layer, counter_of_turns):
    """
    check the part for closed geometry, isolate each line (by default expecting Nut(groove)) to a separate layer that starts with the old layer name; delete the old line; check if this path is closed.
    If the path is closed, get the longest line which will be a reference line for turning and later sewing. Turn it horizontal if it's not already.

    :param NutX_paths_count: number of paths detected
    :type NutX_paths_count: int
    :param part: part that will be turned according to a reference line
    :type part: str
    :param layer_name: only the layer name, without "Part1//"
    :type layer_name: str
    :param layer: layer that is being examined
    :type layer: str
    :param counter_of_turns: counting how much times the part was turned, to catch cases where the part has non-parallel lines
    :type counter_of_turns: int
    :return: counter_of_turns
    :rtype: int
    """
    closed_geoms = []
    new_layers = []
    do_debug()
    for i in range(NutX_paths_count):
        new_layer = gdb.add_layer(part, f"{layer_name}_new_layer_{i+1}")
        path.extract(layer, i+1, new_layer, erase_source_object = True)
        new_layers.append(new_layer)
        NutX_new_lines = gdb.get_entities(new_layer)
        if path.is_closed(new_layer):
            closed_geoms.append(new_layer)
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
        else:
            counter_of_turns = check_opened_geom(NutX_new_lines, part, counter_of_turns)
    return counter_of_turns


def is_horisontal(NutX_line):
    """
    Check if the y-coordinate of the start point and the y-coordinate of the end point have the same value. If it's same, the line is horisontal within the coordinate system the line is in.

    :param NutX_line: line to check (by default expecting Nut(groove))
    :type NutX_line: str
    :return: True if line is horisontal
    :rtype: bool
    """
    start_nutx_line = gdb.get_start_point(NutX_line)
    end_nutx_line = gdb.get_end_point(NutX_line)
    return round(start_nutx_line.y, 8) == round(end_nutx_line.y, 8)


def is_vertical(NutX_line): #if start and end lines are on the same x level they're vertical
    """
    Check if the x-coordinate of the start point and the x-coordinate of the end point have the same value. If they are the same, the line is vertical within the coordinate system the line is in.

    :param NutX_line: line to check (by default expecting Nut(groove))
    :type NutX_line: str
    :return: True if line is vertical
    :rtype: bool
    """
    start_nutx_line = gdb.get_start_point(NutX_line)
    end_nutx_line = gdb.get_end_point(NutX_line)

    return round(start_nutx_line.x, 8) == round(end_nutx_line.x, 8)

def turn(part, NutX_line):
    """
    Turn the whole part that contains the reference line by the negative degree of the angle of the reference line (by default expecting the line to be Nut(groove)).

    :param part: part that will be turned according to a reference line
    :type part: str
    :param NutX_lines: list of lines
    :type NutX_lines: list
    :return: None
    """
    angle_to_turn = gdb.get_angle(NutX_line)
    cad.rotate_piece(part, 0, 0, -angle_to_turn, create_copy=False)
    gdb.set_note(part, 'NRAN', '0')


def check_if_rectangle(new_layer):
    """
    Check if the closed geometry is rectangular. Count the lines and check if there are 4 of them and if they are strictly vertical and horizontal.

    :param new_layer: layer created by this program with a goal to isolate Nut(groove) lines
    :type new_layer: str
    :return: True if it is a rectangle
    :rtype: bool
    """
    straight_lines = []
    lines = gdb.get_entities(new_layer)
    if len(lines) == 4:
        for line in lines: # i can just take odd lines?..
            if is_horisontal(line) or is_vertical(line):
                straight_lines.append(line) #can delete that from list to not clutter up the memory
        if len(straight_lines) == 4:
            return True
        else: #lines are not straight
            dlg.output_box(f"Eine oder mehrere Linien sind nicht gerade, bitte überprüfen Sie die Figur. Sie sollten es entweder manuell einrichten oder den Support kontaktieren.")

    else: #not 4 lines
        dlg.output_box(f"Es sollten 4 Linien in der Figur sein, aber es sind nicht 4. Bitte überprüfen Sie die Figur. Sie sollten es entweder manuell einrichten oder den Support kontaktieren.")
    return False


if __name__ == '__main__':
    main()
