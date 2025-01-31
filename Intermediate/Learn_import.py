#first file: learn_import_1.py
def function_1(name):
    print (f"\nHallo, {name}!")


#second file: learn_import_2.py
from learn_import_1 import function_1 as f1   #f1 is an alias
from helloworld import *   # * = all

f1("Max")

calculator()
