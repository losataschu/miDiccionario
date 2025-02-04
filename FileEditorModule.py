# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:13:22 2025

@author: losat
"""

import json
import ValidatingModule as valid_m

def add_entry(filename, text, day, month, year):
    my_entries = load_entries(filename)
    #print(my_entries["Entradas"])
    try:
        if valid_m.validate_entry(my_entries, text):
            raise ValueError("Please enter a new entry.")
        #TODO: check the correct numerical input.
        my_entries["Entradas"].append({"palabra" : text, "fecha" : [day, month, year]})
        with open(filename, "w") as file_new:
            json.dump(my_entries, file_new, indent=2)
    except ValueError as e:
        print(f"Existing entry: {e}")

def delete_entry(filename, text):
    my_entries = load_entries(filename)
    #print(my_entries["Entradas"])
    try:
        deleted_entry = check_delete_entry(my_entries, text)
        if not isinstance(deleted_entry, dict):
            raise ValueError("No existing entry with that text.")
        my_entries["Entradas"].remove(deleted_entry)
        with open(filename, "w") as file_new:
            json.dump(my_entries, file_new, indent=2)
    except ValueError as e:
        print(f"Not found: {e}")

def load_entries(filename):
    with open(filename, 'r') as file:
        return json.loads(file.read())

def check_delete_entry(entries, text):
    selected_entry = None
    for entry in entries["Entradas"]:
        if entry["palabra"] == text:
            selected_entry = entry
            break
    return selected_entry
