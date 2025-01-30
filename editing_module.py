# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:13:22 2025

@author: losat
"""

import json
import warning_module as wm

def add_entry(filename, text, day, month, year):
    my_entries = load_entries(filename)
    #print(my_entries["Entradas"])
    if check_entry(my_entries, text):
       return wm.print_abort("Please enter a new entry.")
    #TODO: check the correct numerical input.
    my_entries["Entradas"].append({"palabra" : text, "fecha" : [day, month, year]})
    with open(filename, "w") as file_new:
        json.dump(my_entries, file_new, indent=2)

def delete_entry(filename, text):
    my_entries = load_entries(filename)
    #print(my_entries["Entradas"])
    my_entries = check_delete_entry(my_entries, text)
    with open(filename, "w") as file_new:
        json.dump(my_entries, file_new, indent=2)

def load_entries(filename):
    with open(filename, 'r') as file:
        return json.loads(file.read())

def check_entry(entries, text):
    is_stored = False
    for entry in entries["Entradas"]:
        if entry["palabra"] == text:
            is_stored = True
            break
    return is_stored

def check_delete_entry(entries, text):
    is_stored = False
    for entry in entries["Entradas"]:
        if entry["palabra"] == text:
            is_stored = True
            entries["Entradas"].remove(entry)
            break
    if not is_stored:
        wm.print_abort("No existing entry with that text.")
    return entries
