# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:57:21 2025

@author: losat
"""
from itertools import chain
from collections import defaultdict
import FormatDisplayModule as fdm
from warning_module import print_abort
import ValidatingModule as valid_m

ATTRIBUTE_STRATEGIES = {"category" : lambda entry : entry.category.lower(),
                         "initial_letter" : lambda entry : entry.text[0].lower(),
                         "year" : lambda entry : entry.date[2],
                         "month" : lambda entry : entry.date[1],
                         "day" : lambda entry : entry.date[0],
                         "monthly" : lambda entry : (entry.date[0], entry.date[1]),
                         "date" : lambda entry : tuple(entry.date)
                         }
ATTRIBUTE_FILTER_LOGIC = {"category" : lambda text : text.lower(),
                         "initial_letter" : lambda letter : letter.lower(),
                         "year" : lambda number : number,
                         "month" : lambda number : number,
                         "day" : lambda number : number,
                         "monthly" : lambda date : (date[0], date[1]),
                         "date" : lambda date : tuple(date)
                         }
ATTRIBUTE_VALIDATION = {"category" : valid_m.validate_category,
                        "initial_letter" : valid_m.validate_init_letter,
                        "year" : valid_m.validate_date_number,
                        "month" : valid_m.validate_month,
                        "day" : valid_m.validate_day,
                        "date": valid_m.validate_date_list,
                        "monthly" : valid_m.validate_month_tuple
                        }

# function that creates and prints the resulting table
def create_print_entry_table(entry_list):
    entries_vocab = fdm.VocabularyEntries(entry_list)
    table_with_entries = entries_vocab.create_formatted_table()
    # entries_vocab.show_table(table_with_entries[0], table_with_entries[1], table_with_entries[2])
    entries_vocab.show_table_tabulate(table_with_entries[0], table_with_entries[1])
    
def index_filter_attributes(entry_list):
    index = create_index_dict()
    for entry in entry_list:
        update_index_add(index, entry)
    return index

def create_index_dict():
    index = {}
    for attribute in ATTRIBUTE_STRATEGIES.keys():
        index[attribute] = defaultdict(list)
    return index

def update_index_add(indexed_entries, entry):
    for attribute, strategy in ATTRIBUTE_STRATEGIES.items():
        key = strategy(entry)
        indexed_entries[attribute][key].append(entry)

def update_index_remove(indexed_entries, text):
    entry = check_delete_entry(indexed_entries, text)
    for attribute, strategy in ATTRIBUTE_STRATEGIES.items():
        key = strategy(entry)
        indexed_entries[attribute][key].remove(entry)

def check_delete_entry(indexed_entries, text):
    selected_entry = None
    for entry in chain.from_iterable(indexed_entries["category"].values()):
        if entry.__repr__() == text:
            selected_entry = entry
            break
    return selected_entry

# this function redirects the filtering to the respective method
def filter_entries(entry_dict, attribute, value):
    indices = entry_dict.indexed_entries
    try:
        if indices is None:
            raise NotImplementedError("Index not initialized. Run setup_filtering() first.")
        if attribute not in indices.keys():
            return print_abort("No filter for that attribute.")
        filter_and_display_table(indices, attribute, value)
    except NotImplementedError as e:
        print(f"{e}")
    except ValueError as e:
        print(f"Validation error: {e}")
        
def filter_and_display_table(indexed_entries, attribute, value):
    filtered_vocabulary = filter_by_attribute(indexed_entries, attribute, value)
    #this logic creates the table if and only if the filtered list is not empty    
    if filtered_vocabulary:
        create_print_entry_table(filtered_vocabulary)
        return
    else:
        print("No entries found for that attribute!")

def filter_by_attribute(indexed_entries, attribute, value):
    filtered_entries = None
    if validate_value(attribute, value):
        filtered_entries = indexed_entries[attribute].get(ATTRIBUTE_FILTER_LOGIC[attribute](value), [])
    return filtered_entries

def validate_value(attribute, value):
    return ATTRIBUTE_VALIDATION[attribute](value)

# def debug_key(entry):
#     print(f"Text: {entry.text}, Key Used: {entry.text.lower()}")
#     return entry.text.lower()

# this function redirects the sorting to the respective method
def sort_entries(entry_list, attribute):
    sorted_vocabulary = []
    match attribute:
        case "alphabetical":
            sorted_vocabulary = sorted(entry_list, key=lambda x: x.text.lower())
            # sorted_vocabulary = sorted(entries_vocab, key=debug_key)
            # for entry in sorted_vocabulary:
            #     print(f"Sorted Entry: {entry.text}")
        case "alphabetical_inv":
            sorted_vocabulary = sorted(entry_list, key=lambda x: x.text, reverse=True)
        case "oldest":
            sorted_vocabulary = sorted(entry_list, key=lambda x: (x.date[2], x.date[1], x.date[0]))
        case "newest":
            sorted_vocabulary = sorted(entry_list, key=lambda x: (x.date[2], x.date[1], x.date[0]), reverse=True)
        case _:
            return print_abort("No method for that attribute.")
    
    #this logic creates the table if and only if the filtered list is not empty    
    if sorted_vocabulary:
        create_print_entry_table(sorted_vocabulary)
