from company import gdb
from sclcore import do_debug
do_debug()
parts  = gdb.get_entities()
a = len(parts)
for part in parts:
    for a in part:
        new_name = gdb.get_new_name(part, hint_name="Lay")
        gdb.add_layer(part, new_name)

#def get_new_name(curr_obj, hint_name=""):
#(f'{part}\\contour'))     for lines on lay
#gdb.get_entities(part)    for lay
