# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:57:21 2025

@author: losat
"""
import vocabulary_table as vt
from warning_module import print_abort

# function that creates and prints the resulting table
def list_entries(vocab_list):
    vocab_table = vt.VocabularyList(vocab_list)
    table_elements = vocab_table.create_table()
    vocab_table.show_table(table_elements[0], table_elements[1], table_elements[2])

# this function redirects the filtering to the respective method
def filter_entries(vocab_list, attribute, value):
    filtered_vocabulary = []
    match attribute:
        case "category":
            if value.lower() in ["noun", "other"]:
                filtered_vocabulary = [entry for entry in vocab_list if entry.category.lower() == value.lower()]
            else:
                return print_abort("Invalid category!")
        case "initial_letter": 
            if len(value) != 1:
                return print_abort("Please type only one letter!")
            filtered_vocabulary = [entry for entry in vocab_list if entry.text[0].lower() == value.lower()]
        case "year" | "month" | "day":
            if value < 0:
                return print_abort("Please enter a positive number!")
            filtered_vocabulary = date_filter(vocab_list, attribute, value)
        case "monthly" | "date":
            try:
                for i in value:
                    if i < 0:
                        return print_abort("Please enter positive numbers!")
                filtered_vocabulary = date_filter(vocab_list, attribute, value)
            except TypeError as e:
                print(e)
        case _:
            return print_abort("No method for that attribute.")
    
    #this logic creates the table if and only if the filtered list is not empty    
    if filtered_vocabulary:
        list_entries(filtered_vocabulary)
    else:
        print("No entries found for that attribute!")

def date_filter(vocab_list, attribute, value):
    filtered_vocabulary = []
    #print(value)
    match attribute:
        case "year":
            for i in vocab_list:
                if i.date[2] == value:
                    filtered_vocabulary.append(i)
        case "month":
            for i in vocab_list:
                if value == 0 or value > 12:
                    return print_abort("Invalid month number!")
                elif i.date[1] == value:
                    filtered_vocabulary.append(i)
        case "day":
            for i in vocab_list:
                if value == 0 or value > 31:
                    return print_abort("Invalid day number!")
                if i.date[0] == value:
                    filtered_vocabulary.append(i)
        case "monthly":
            if len(value) != 2:
                return print_abort("Please enter a day number followed by a month number")
            elif value[1] == 0 or value[1] > 12 or value[0] == 0 or value[0] > 31:
                return print_abort("Invalid numbers!")
            else:
                for i in vocab_list:
                    if i.date[0] == value[0] and i.date[1] == value[1]:
                        filtered_vocabulary.append(i)
        case "date":
            if len(value) != 3:
                print_abort("Please enter a day number followed by a month number and a year")
            elif value[1] == 0 or value[1] > 12 or value[0] == 0 or value[0] > 31:
                return print_abort("Invalid numbers!")
            else:
                for i in vocab_list:
                    if i.date == value:
                        filtered_vocabulary.append(i)
        case _:
            return print_abort("Invalid time category!")
    return filtered_vocabulary