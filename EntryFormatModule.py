# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:44:12 2025

@author: losat
"""
import EntryFactory as efact

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
    
def build_entry(text, date_list):
    entry_to_append = None
    if is_noun(text):
        noun_parts = text.split(" ", 1)
        entry_to_append =  efact.Noun(article=noun_parts[0], text=noun_parts[1],
                                       date=date_list, category="Noun")
    else:
        entry_to_append = efact.Entry(text=text, date=date_list,
                                category="Other")
    return entry_to_append
    