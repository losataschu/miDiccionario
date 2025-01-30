# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:57:21 2025

@author: losat
"""
import vocabulary_table as vt
from warning_module import print_abort
import validating_module as valid_m

# function that creates and prints the resulting table
def list_entries(vocab_list):
    vocab_table = vt.VocabularyList(vocab_list)
    table_elements = vocab_table.create_table()
    vocab_table.show_table(table_elements[0], table_elements[1], table_elements[2])

# this function redirects the filtering to the respective method
def filter_entries(vocab_list, attribute, value):
    try:
        match attribute:
            case "category":
                valid_m.validate_category(value)
                filtered_vocabulary = [entry for entry in vocab_list if entry.category.lower() == value.lower()]
            case "initial_letter": 
                valid_m.validate_init_letter(value)
                filtered_vocabulary = [entry for entry in vocab_list if entry.text[0].lower() == value.lower()]
            case "year" | "month" | "day":
                valid_m.validate_date_number(value)
                filtered_vocabulary = date_filter(vocab_list, attribute, value)
            case "date":
                valid_m.validate_date_list(value)
                filtered_vocabulary = date_filter(vocab_list, attribute, value)
            case "monthly":
                valid_m.validate_month_tuple(value)
                filtered_vocabulary = date_filter(vocab_list, attribute, value)
            case _:
                return print_abort("No method for that attribute.")
    
        #this logic creates the table if and only if the filtered list is not empty    
        if filtered_vocabulary:
            list_entries(filtered_vocabulary)
        else:
            print("No entries found for that attribute!")
    except ValueError as e:
        print(f"Validation error: {e}")

def date_filter(vocab_list, attribute, value):
    filtered_vocabulary = []
    #print(value)
    match attribute:
        case "year":
            for i in vocab_list:
                if i.date[2] == value:
                    filtered_vocabulary.append(i)
        case "month":
            valid_m.validate_month_tuple([1, value])
            for i in vocab_list:
                if i.date[1] == value:
                    filtered_vocabulary.append(i)
        case "day":
            valid_m.validate_month_tuple([value, 12])
            for i in vocab_list:
                if i.date[0] == value:
                    filtered_vocabulary.append(i)
        case "monthly":
            valid_m.validate_month_tuple(value)
            for i in vocab_list:
                if i.date[0] == value[0] and i.date[1] == value[1]:
                    filtered_vocabulary.append(i)
        case "date":
            valid_m.validate_date_list(value)
            for i in vocab_list:
                if i.date == value:
                    filtered_vocabulary.append(i)
        case _:
            return print_abort("Invalid time category!")
    return filtered_vocabulary

# def debug_key(entry):
#     print(f"Text: {entry.text}, Key Used: {entry.text.lower()}")
#     return entry.text.lower()

# this function redirects the sorting to the respective method
def sort_entries(vocab_list, attribute):
    filtered_vocabulary = []
    match attribute:
        case "alphabetical":
            filtered_vocabulary = sorted(vocab_list, key=lambda x: x.text.lower())
            # filtered_vocabulary = sorted(vocab_list, key=debug_key)
            # for entry in filtered_vocabulary:
            #     print(f"Sorted Entry: {entry.text}")
        case "alphabetical_inv":
            filtered_vocabulary = sorted(vocab_list, key=lambda x: x.text, reverse=True)
        case "oldest":
            filtered_vocabulary = sorted(vocab_list, key=lambda x: (x.date[2], x.date[1], x.date[0]))
        case "newest":
            filtered_vocabulary = sorted(vocab_list, key=lambda x: (x.date[2], x.date[1], x.date[0]), reverse=True)
        case _:
            return print_abort("No method for that attribute.")
    
    #this logic creates the table if and only if the filtered list is not empty    
    if filtered_vocabulary:
        list_entries(filtered_vocabulary)
