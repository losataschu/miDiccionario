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
    initial_count = len(my_entries["Entradas"])
    my_entries["Entradas"] = [entry for entry in my_entries["Entradas"] if 
                              entry["palabra"] != text]
    if len(my_entries["Entradas"]) == initial_count:
        print("Not found: no existing entry with that text.")
        return
    with open(filename, "w") as file_new:
        json.dump(my_entries, file_new, indent=2)
    print(f"Entry '{text}' deleted successfully.")

def load_entries(filename):
    with open(filename, 'r') as file:
        return json.loads(file.read())
