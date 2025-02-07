# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:32:22 2025

@author: losat
"""

def validate_category(value):
    valid_categories = ["noun", "other"]
    if value.lower() not in valid_categories:
        raise ValueError(f"Invalid category! Allowed categories are: {valid_categories}")
    return True
        
def validate_init_letter(value):
    if len(value) != 1:
        raise ValueError("Please enter only one letter!")
    return True

def validate_date_number(value):
    if not isinstance(value, int) or value < 0:
        raise ValueError("A date parameter cannot be negative!")
    return True

def validate_month_tuple(value):
    if not isinstance(value, list) or len(value) != 2:
        raise ValueError("Recall the correct format: [day, month].")
    for i in value:
        validate_date_number(i)
    day, month = value
    if not (1 <= day <= 31 and 1 <= month <= 12):
        raise ValueError("Invalid date! Ensure your month or day number lies within a valid range.")
    return True

def validate_date_list(value):
    if not isinstance(value, list) or len(value) != 3:
        raise ValueError("Date must have the following format: [day, month, year].")
    for i in value:
        validate_date_number(i)
    day, month, year = value
    validate_month_tuple([day, month])
    return True

def validate_entry(entry_list, text):
    for entry in entry_list:
        if entry.__repr__() == text:
            return True
