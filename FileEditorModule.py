# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:13:22 2025

@author: losat
"""

import json
import DictionaryCore as dcore
import ValidatingModule as valid_m
import FilterSortModule as fsm
from warning_module import print_abort

def add_entry(entry_dict, text, day, month, year):
    try:
        if valid_m.validate_entry(entry_dict.all_entries, text):
            raise ValueError("Please enter a new entry.")
        #TODO: check the correct numerical input.
        new_entry = dcore.build_entry(text, [day, month, year])
        add_and_index_entry(entry_dict, new_entry)
    except ValueError as e:
        print(f"Existing entry: {e}")

def add_and_index_entry(entry_dict, entry):
    if entry_dict.indexed_entries is not None:
        fsm.update_index_add(entry_dict.indexed_entries, entry)
    entry_dict.all_entries.append(entry)    

def delete_entry(entry_dict, text):
    entry_list = entry_dict.all_entries
    initial_count = len(entry_list)
    entry_list[:] = [entry for entry in entry_list if 
                              entry.__repr__() != text]
    if len(entry_list) == initial_count:
        return print_abort("Not found: no existing entry with that text.")
    if entry_dict.indexed_entries is not None:
        fsm.update_index_remove(entry_dict.indexed_entries, text)
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
        