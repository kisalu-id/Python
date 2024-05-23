import os #os.path as abc
import json
from os import path #can write path.something
from sclcore import do_debug
from company import dlg
#try except
#add more buttons?
#structure

def extract_unique_abbreviation(file_name, abbreviations_list):
    capital_letters = []
    for char in file_name:
        if char.isupper():
            capital_letters.append(char)
    abbreviation = "".join(capital_letters)
    return abbreviation
    """except:
        dlg.output_box("Error in extract_unique_abbreviation")
        return ""
        """

def append_file_name(abbreviation, value):
    if value.startswith(abbreviation):
        return value
    else:
        try:
            modified_value = f"{abbreviation}{value}"
            return modified_value
        except:
            dlg.output_box("Error in append_file_name")
            return 0

def remove_file_name(abbreviation, value):
    try:
        if value.startswith(abbreviation):
            value = value[len(abbreviation):]
        return value
    except:
        dlg.output_box("Error in remove_file_name")
        return value


def main_function():
    do_debug()
    file_paths = dlg.select_file("msg_files (*.msg)|*.msg", initial_dir=r"C:\ProgramData\...\Config\Language\Deu", open_file=True, select_multiple=True)
    file_paths = file_paths.split(",")
    file_paths = [fp for fp in file_paths if fp] #filter out empty paths
    abbreviations_list = []
    original_values_dictionary = {} #dictionary to store original values for each file
    abbreviations_list_exists = False
    counter = 1
    if counter == 1: #modify
        for file_path in file_paths: #for each .msg file
            if isinstance(file_path, str):
                file_name = os.path.splitext(os.path.basename(file_path))[0] #extract the file name without extension
                with open(file_path, "r") as f:
                    abbreviation = extract_unique_abbreviation(file_name, abbreviations_list) #iterate through each value, add abbr to the value
                    abbreviations_list_exists = True
                    i = 1
                    if abbreviation in abbreviations_list:
                        while abbreviation in abbreviations_list:
                            abbreviation = f"{abbreviation}{i}"
                            i += 1
                            continue
                    abbreviations_list.append(abbreviation)

                    lines = f.readlines()
                    original_values_dictionary[file_path] = lines.copy()
                    modified_values = []
                    for i, line in enumerate(lines):
                        try:
                            parts = line.split(": ", 1)
                            if len(parts) == 2:
                                value = parts[1].strip().strip('"').rstrip(',"')
                                modified_value = append_file_name(abbreviation, value) #DCOk
                                modified_values.append(f'{parts[0]}: "{modified_value}"')
                                if i < (len(lines)-2):
                                    modified_values.append(',')
                                modified_values.append('\n')
                            elif len(parts) >= 3:
                                dlg.output_box("in main parts >=3")
                            else:
                                modified_values.append(line)
                        except:
                            dlg.output_box("Block 1 error")
                            continue
                    with open(file_path, "w") as f:
                        f.writelines(modified_values)


    counter = 2
    if counter == 2: #rewrite orig values stored in a dictionary, ONLY execute this block together with 1st, in 1 go! so set counter to 1, then to 2
        try:
            file_path = file_paths[0]
            for file_path in file_paths:
                if file_path in original_values_dictionary:
                    original_lines = original_values_dictionary[file_path].copy()
                    with open(file_path, "w") as f:
                        f.writelines(original_lines)
        except:
            dlg.output_box("Block 2 error: you can only execute this block together with 1st, in 1 go")
            #!!! make the program run block 3
#if i'll want to just remove abbr, insert functions: extract_unique_abbreviation and remove_file_name


    counter = 0
    if counter == 3: #remove abbr, can exeture in 1 go after 1st block, or separately
#    try:
        file_path = file_paths[0]
        for j, file_path in enumerate(file_paths):
            with open(file_path, "r") as f:
                file_name = os.path.splitext(os.path.basename(file_path))[0]  #extract the file name without extension
                if not abbreviations_list_exists: #if that list doesnt exist
                    abbreviation = extract_unique_abbreviation(file_name, abbreviations_list)
                    i = 1
                    if abbreviation in abbreviations_list:
                        while abbreviation in abbreviations_list:
                            abbreviation = f"{abbreviation}{i}"
                            i += 1
                            continue
                    abbreviations_list.append(abbreviation)
                else:
                    abbreviation = abbreviations_list[j]
                lines = f.readlines()
                original_values = []
                for x, line in enumerate(lines):
                    parts = line.split(": ", 1)
                    if len(parts) == 2:
                        value = parts[1].strip().strip('"').rstrip(',"')
                        value = remove_file_name(abbreviation, value)
                        original_values.append(f'{parts[0]}: "{value}"')
                        if x < (len(lines)-2):
                            original_values.append(',')
                        original_values.append('\n')
                    elif len(parts) >= 3:
                        dlg.output_box("in main parts >=3")
                    else:
                        original_values.append(line)
                with open(file_path, "w") as f:
                    f.writelines(original_values)
        #except:
        #    dlg.output_box("Block 3 Error")
        
        
if __name__ == '__main__':
    main_function()
