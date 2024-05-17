import os #os.path as abc
import json
from os import path #can write path.etwas
from sclcore import do_debug
from company import dlg

def extract_values(line):
    #split with :
    #get 2nd val
    #remove ""
    value = 
    if i startswith("):
        print(f.readline())
        line = txt.split(", ")
        
        value = line[1]


def extract_unique_abbreviation(file_name):
    capital_letters = []
    for char in file_name:
        if char.isupper():
            capital_letters.append(char)
    abbreviation = "".join(capital_letters)
    #create a list of abbreviations, iterate through it, if match: add  next small letter?
    #    capital_letters.append(char+1)
    try:
        return abbreviation
    except:
        dlg.output_box("Error in extract_unique_abbreviation")



def append_file_name(abbreviation, value):
    modified_value = []



    try:
        return modified_value
    except:
        dlg.output_box("Error in append_file_name")



def remove_file_name(abbreviation, value):





def main_function():
    file_paths = [
        r"C:\ProgramData\...\ComponentDeu.msg",
        r"C:\ProgramData\...\NestDeu.msg",
        r"C:\ProgramData\...\ABDeu.msg",
        r"C:\ProgramData\...\Edit5aDeu.msg",
        r"C:\ProgramData\...\CDDeu.msg",
        r"C:\ProgramData\...\GBdCommDeu.msg",
        r"C:\ProgramData\...\KDgfCDeu.msg",
        r"C:\ProgramData\...\GlobDeu.msg",
        r"C:\ProgramData\...\GrafDeu.msg",
        r"C:\ProgramData\...\ListLabelDeu.msg",
        r"C:\ProgramData\...\OptDeu.msg",
        r"C:\ProgramData\...\VmillMgrDeu.msg",
    ]

    for file_path in file_paths: #for each .msg file
        #open
        f = open(file_name, "r")
        #extract the file name without extension
        file_name = os.path.splitext(os.path.basename(file_path))[0]  
        print(os.path.splitext(file_name)[0])
        #get abbr
        abbreviation = extract_unique_abbreviation(file_name)
        #iterate through each value, add abbr to the value
        #?create new file, copy new values there?
        lines = file_name.readlines()
        for line in lines:
            value = extract_values(file_path):

            modified_value = append_file_name(abbreviation, value)
            print(f"Modified value: {modified_value}")

        # !!! if "remove file name" is pressed:
        # !!! do a better logic
        lines = file_name.readlines()
        for line in lines:
            value = remove_file_name(abbreviation, modified_value)
            print(f"Reversed value: {value}")


        f.close()



if __name__ == '__main__':

    main_function()
