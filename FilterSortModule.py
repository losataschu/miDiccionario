# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:57:21 2025

@author: losat
"""
import VocabularyTable as vt
from warning_module import print_abort
import ValidatingModule as valid_m

# function that creates and prints the resulting table
def create_print_entry_table(entries_vocab):
    entries_vocab = vt.VocabularyEntries(entries_vocab)
    table_with_entries = entries_vocab.create_formatted_table()
    entries_vocab.show_table(table_with_entries[0], table_with_entries[1], table_with_entries[2])

# this function redirects the filtering to the respective method
def filter_entries(entries_vocab, attribute, value):
    try:
        match attribute:
            case "category":
                filtered_vocabulary = filter_by_category(entries_vocab, value)
            case "initial_letter": 
                filtered_vocabulary = filter_by_initial_letter(entries_vocab, value)
            case "year":
                filtered_vocabulary = filter_by_year(entries_vocab, value)
            case "month":
                filtered_vocabulary = filter_by_month(entries_vocab, value)
            case "day":
                filtered_vocabulary = filter_by_day(entries_vocab, value)
            case "date":
                filtered_vocabulary = filter_by_exact_date(entries_vocab, value)
            case "monthly":
                filtered_vocabulary = filter_by_day_month(entries_vocab, value)
            case _:
                return print_abort("No filter for that attribute.")
    
        #this logic creates the table if and only if the filtered list is not empty    
        if filtered_vocabulary:
            create_print_entry_table(filtered_vocabulary)
        else:
            print("No entries found for that attribute!")
    except ValueError as e:
        print(f"Validation error: {e}")

def filter_by_category(entry_list, value):
    valid_m.validate_category(value)
    filtered_entry_list = [entry for entry in entry_list if
                           entry.category.lower() == value.lower()]
    return filtered_entry_list

def filter_by_initial_letter(entry_list, value):
    valid_m.validate_init_letter(value)
    filtered_entry_list = [entry for entry in entry_list if
                           entry.text[0].lower() == value.lower()]
    return filtered_entry_list

def filter_by_year(entry_list, value):
    valid_m.validate_date_number(value)
    filtered_entry_list = [entry for entry in entry_list if entry.date[2] == value]
    return filtered_entry_list

def filter_by_month(entry_list, value):
    valid_m.validate_date_number(value)
    valid_m.validate_month_tuple([1, value])
    filtered_entry_list = [entry for entry in entry_list if entry.date[1] == value]
    return filtered_entry_list

def filter_by_day(entry_list, value):
    valid_m.validate_date_number(value)
    valid_m.validate_month_tuple([value, 12])
    filtered_entry_list = [entry for entry in entry_list if entry.date[0] == value]
    return filtered_entry_list

def filter_by_day_month(entry_list, value):
    valid_m.validate_month_tuple(value)
    filtered_entry_list = [entry for entry in entry_list if
                           (entry.date[0] == value[0] and entry.date[1] == value[1])]
    return filtered_entry_list

def filter_by_exact_date(entry_list, value):
    valid_m.validate_date_list(value)
    filtered_entry_list = [entry for entry in entry_list if entry.date == value]
    return filtered_entry_list

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
