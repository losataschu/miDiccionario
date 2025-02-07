# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:13:22 2025

@author: losat
"""

import json
import EntryFormatModule as eformat
import ValidatingModule as valid_m

def add_entry(entry_list, text, day, month, year):
    try:
        if valid_m.validate_entry(entry_list, text):
            raise ValueError("Please enter a new entry.")
        #TODO: check the correct numerical input.
        new_entry = eformat.build_entry(text, [day, month, year])
        entry_list.append(new_entry)
    except ValueError as e:
        print(f"Existing entry: {e}")

def delete_entry(entry_list, text):
    initial_count = len(entry_list)
    entry_list[:] = [entry for entry in entry_list if 
                              entry.__repr__() != text]
    if len(entry_list) == initial_count:
        print("Not found: no existing entry with that text.")
        return
    print(f"Entry '{text}' deleted successfully.")

def save_entries_to_file(entry_list, filename):
    #TODO create JSON-formatted list
    my_entries = []
    for entry in entry_list:
        json_entry = {"palabra" : entry.__repr__(), "fecha" : entry.date}
        my_entries.append(json_entry)
    my_dictionary = {"Entradas" : my_entries}
    with open(filename, "w") as file_new:   
        json.dump(my_dictionary, file_new, indent=2)
        
def load_entries(filename):
    with open(filename, 'r') as file:
        return json.loads(file.read())
        