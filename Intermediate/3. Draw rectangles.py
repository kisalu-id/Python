from company import dlg                 # module to create dialogs
from company import gdb                 # standard database operations
from company.gdb import cad             # drawing functions
from sclcore import do_debug            # debugging purposes
from sclcore import Vec3
import ewd

# program that asks the user how often he wants to repeat the next question
# then it asks for dimensions of a rectangle
# then we create a new easywood part and draw a rectangle in the correct dimensions
# if the values entered are not formally correct we should output a message warning the user and cancel

#  inputs = ask_for_inputs()
#  create_rectangles(inputs)

def draw_rectangle(part_number):
    a = dlg.input_box("a-Wert eingeben: ", "a")
    b = dlg.input_box("b-Wert eingeben: ", "b")
    cad.add_rectangle(f"Part{part_number}\\Lay1", Vec3(0, 0, 0), width=a, length=b, material=cad.StandardColors.FUCHSIA)

do_debug()

def main():
    ewd.new_project()
    times = dlg.input_box("Wie oft willst du die Frage beantworten?", "Mal")
    for part_number in range(0, int(times)):
        if not gdb.exist(f"Part{part_number}"):
            gdb.add_part(f"Part{part_number}")
        draw_rectangle(part_number)

if __name__ == '__main__':
    main()
