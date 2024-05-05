from company import dlg
from company import gdb
from company.gdb import cad
from sclcore import do_debug, Vec3
import os
#to read:  data open/read python

# program that imports a csv
# for each line in the csv we create a rectangle with the dimensions in that line
# if there is a dxf path in the line we import a dxf instead

# then we run an autocam through all pieces
# position them on the table on the top right corner
# and generate the cnc file

do_debug()

def main_function():
    do_debug()

    file = open(r"C:\Users\name\Desktop\folder\test.csv", "r")
    lines = file.readlines()
    i = 1
    for line in lines:
        #dlg.output_box(x)
        line_values = line.split(",")
        point_x = float(line_values[0])
        point_y = float(line_values[1])
        point_z = float(line_values[2])
        width = float(line_values[3])
        length = float(line_values[4])
        angle = float(line_values[5])
        fillet_radious = float(line_values[6])

        if not gdb.exist(f"Part{i}"):
            gdb.add_part(f"Part{i}")
        cad.add_rectangle(f'Part{i}\Lay1',Vec3(point_x,point_y,point_z),width,length,angle,fillet_radious)
        i+=1

if __name__ == '__main__':

    main_function()
