from datetime import datetime
from company import gdb
from company import dlg
from company.gdb import cad
from company.gdb.view import redraw_window, zoom_all
from config import run_config
from sclcore import do_debug

def main():
    do_debug()
    error_in_check_x_grooves = False
    parts = gdb.get_entities()
    for part in parts:
        layers = gdb.get_entities(part)
        for layer in layers:
            layer_name = layer.split("\\")
            layer_name = layer_name[-1]
            if layer_name.upper().startswith("NUTX"):
                NutX_lines = gdb.get_entities(layer)
                if len(NutX_lines) == 1:
                    NutX_line = NutX_lines[0]
                else:
                    error_in_check_x_grooves = True

                start_nutx_line = gdb.get_start_point(NutX_line) #vec3 x y z
                end_nutx_line = gdb.get_end_point(NutX_line)
                if start_nutx_line.y != end_nutx_line.y: #check if the line isn't horisontal
                    angle_to_turn = gdb.get_angle(NutX_line)
                    cad.rotate_piece(part, 0, 0, -angle_to_turn, create_copy=False)
                gdb.set_note(part, 'NRAN', '0')
    if error_in_check_x_grooves:
        dlg.output_box(f"More than 1 line on layer {layer}")

if __name__ == '__main__':
    main()
