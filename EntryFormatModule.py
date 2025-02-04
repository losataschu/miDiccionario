# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:44:12 2025

@author: losat
"""

def count_words(text):
    if len(text) == 0:
        return 0
    words = 1
    for letter in text:
        if letter == ' ' and text[0] != letter and text[-1] != letter:
            words += 1
    return words

# Function to show double-digits for days and months
def adjust_digits(date):
    if len(f'{date}') == 1:
        return f'0{date}'
    else:
        return f'{date}'
    
def is_noun(text):
    if count_words(text) == 2:
        return True
    