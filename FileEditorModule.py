# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:13:22 2025

@author: losat
"""

import json
import DictionaryCore as dcore
import ValidatingModule as valid_m
import FilterSortModule as fsm
import ErrorModule as err_m

def add_entry(entry_dict, text, day, month, year):
    try:
        check_existing_entry(entry_dict.all_entries, text)
        #TODO: check the correct numerical input.
        new_entry = dcore.build_entry(text, [day, month, year])
        add_and_index_entry(entry_dict, new_entry)
    except ValueError as e:
        print(f"Existing entry: {e}")

def check_existing_entry(entry_list, text):
    if valid_m.validate_entry(entry_list, text):
        raise ValueError("Please enter a new entry.")
    return True

def add_and_index_entry(entry_dict, entry):
    if entry_dict.indexed_entries is not None:
        fsm.update_index_add(entry_dict.indexed_entries, entry)
    entry_dict.all_entries.append(entry)    

def delete_entry(entry_dict, text):
    entry_list = entry_dict.all_entries
    initial_count = len(entry_list)
    try:
        entry_list = create_check_new_list(entry_list, text, initial_count)
        if entry_dict.indexed_entries is not None:
            fsm.update_index_remove(entry_dict.indexed_entries, text)
        print(f"Entry '{text}' deleted successfully.")
    except err_m.NotFoundError as e:
        print(f"{e}: no existing entry with that text.")
    
def create_check_new_list(entry_list, text, previous_count):
    entry_list[:] = [entry for entry in entry_list if entry.__repr__() != text]
    if len(entry_list) == previous_count:
        raise err_m.NotFoundError("Not found")
    return entry_list

def save_entries_to_file(entry_dict, filename):
    #TODO how to deal with this using an instance of Dictionary rather than an entry list
    my_entries = []
    for entry in entry_dict.all_entries:
        json_entry = {"palabra" : entry.__repr__(), "fecha" : entry.date}
        my_entries.append(json_entry)
    my_dictionary = {"Entradas" : my_entries}
    with open(filename, "w") as file_new:   
        json.dump(my_dictionary, file_new, indent=2)
        