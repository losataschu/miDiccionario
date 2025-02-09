# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:57:21 2025

@author: losat
"""
from itertools import chain
from collections import defaultdict
import VocabularyTable as vt
from warning_module import print_abort
import ValidatingModule as valid_m


# function that creates and prints the resulting table
def create_print_entry_table(entries_vocab):
    entries_vocab = vt.VocabularyEntries(entries_vocab)
    table_with_entries = entries_vocab.create_formatted_table()
    entries_vocab.show_table(table_with_entries[0], table_with_entries[1], table_with_entries[2])
    
def index_filter_attributes(entries_vocab):
    index = {"category" : defaultdict(list), "initial_letter" : defaultdict(list),
             "year" : defaultdict(list), "month" : defaultdict(list),
             "day" : defaultdict(list), "monthly" : defaultdict(list),
             "date" : defaultdict(list)}
    for entry in entries_vocab:
        index["category"][entry.category.lower()].append(entry)
        index["initial_letter"][entry.text[0].lower()].append(entry)
        index["year"][entry.date[2]].append(entry)
        index["month"][entry.date[1]].append(entry)
        index["day"][entry.date[0]].append(entry)
        index["date"][tuple(entry.date)].append(entry)
        index["monthly"][entry.date[0], entry.date[1]].append(entry)
    return index

# this function redirects the filtering to the respective method
def filter_entries(a_dict, attribute, value):
    indices = a_dict.indexed_entries
    try:
        if indices is None:
            raise NotImplementedError("Index not initialized. Run setup_filtering() first.")
        match attribute:
            case "category":
                valid_m.validate_category(value)
                filtered_vocabulary = indices["category"].get(value.lower(), [])
            case "initial_letter": 
                valid_m.validate_init_letter(value)
                filtered_vocabulary = indices["initial_letter"].get(value.lower(), [])
            case "year":
                valid_m.validate_date_number(value)
                filtered_vocabulary = indices["year"].get(value, [])
            case "month":
                valid_m.validate_date_number(value)
                valid_m.validate_month_tuple([1, value])
                filtered_vocabulary = indices["month"].get(value, [])
            case "day":
                valid_m.validate_date_number(value)
                valid_m.validate_month_tuple([value, 12])
                filtered_vocabulary = indices["day"].get(value, [])
            case "date":
                valid_m.validate_date_list(value)
                filtered_vocabulary = indices["date"].get(tuple(value), [])
            case "monthly":
                valid_m.validate_month_tuple(value)
                filtered_vocabulary = indices["monthly"].get((value[0], value[1]), [])
            case _:
                return print_abort("No filter for that attribute.")
    
        #this logic creates the table if and only if the filtered list is not empty    
        if filtered_vocabulary:
            create_print_entry_table(filtered_vocabulary)
        else:
            print("No entries found for that attribute!")
    except NotImplementedError as e:
        print(f"{e}")
    except ValueError as e:
        print(f"Validation error: {e}")

def update_index_add(indexed_entries, entry):
    indexed_entries["category"][entry.category.lower()].append(entry)
    indexed_entries["initial_letter"][entry.text[0].lower()].append(entry)
    indexed_entries["year"][entry.date[2]].append(entry)
    indexed_entries["month"][entry.date[1]].append(entry)
    indexed_entries["day"][entry.date[0]].append(entry)
    indexed_entries["date"][tuple(entry.date)].append(entry)
    indexed_entries["monthly"][(entry.date[0], entry.date[1])].append(entry)

def update_index_remove(indexed_entries, text):
    entry = check_delete_entry(indexed_entries, text)
    indexed_entries["category"][entry.category.lower()].remove(entry)
    indexed_entries["initial_letter"][entry.text[0].lower()].remove(entry)
    indexed_entries["year"][entry.date[2]].remove(entry)
    indexed_entries["month"][entry.date[1]].remove(entry)
    indexed_entries["day"][entry.date[0]].remove(entry)
    indexed_entries["date"][tuple(entry.date)].remove(entry)
    indexed_entries["monthly"][(entry.date[0], entry.date[1])].remove(entry)
    
def check_delete_entry(entries, text):
    selected_entry = None
    for entry in chain.from_iterable(entries["category"].values()):
        if entry.__repr__() == text:
            selected_entry = entry
            break
    return selected_entry

# def debug_key(entry):
#     print(f"Text: {entry.text}, Key Used: {entry.text.lower()}")
#     return entry.text.lower()

# this function redirects the sorting to the respective method
def sort_entries(entries_vocab, attribute):
    filtered_vocabulary = []
    match attribute:
        case "alphabetical":
            filtered_vocabulary = sorted(entries_vocab, key=lambda x: x.text.lower())
            # filtered_vocabulary = sorted(entries_vocab, key=debug_key)
            # for entry in filtered_vocabulary:
            #     print(f"Sorted Entry: {entry.text}")
        case "alphabetical_inv":
            filtered_vocabulary = sorted(entries_vocab, key=lambda x: x.text, reverse=True)
        case "oldest":
            filtered_vocabulary = sorted(entries_vocab, key=lambda x: (x.date[2], x.date[1], x.date[0]))
        case "newest":
            filtered_vocabulary = sorted(entries_vocab, key=lambda x: (x.date[2], x.date[1], x.date[0]), reverse=True)
        case _:
            return print_abort("No method for that attribute.")
    
    #this logic creates the table if and only if the filtered list is not empty    
    if filtered_vocabulary:
        create_print_entry_table(filtered_vocabulary)
