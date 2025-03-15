# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:50:54 2025

@author: losat
"""

from tabulate import tabulate

ARTICLES = ["der", "die", "das"]

class VocabularyEntries:
    def __init__(self, vocab_entries):
        self.vocab_entries = vocab_entries
    
# Create the table using the entries in the the dictionary
    def create_formatted_table(self):
        row = []
        i = 1
        for entry in self.vocab_entries:
            # TODO: add something to deal with wrong entries
            adjusted_date = adjust_date(entry.date[0], entry.date[1], entry.date[2])
            row.append(create_row(i, entry, adjusted_date))
            i += 1
        return row, ["", "Text", "Date", "Category"]

# Function to show a well-ordered table with my vocabulary   
def show_table(rows, column_names):
    print(tabulate(rows, headers=column_names))

def count_words(text):
    if len(text) == 0:
        return 0
    total_words = 0
    words_in_text = text.split(" ")
    for element in words_in_text:
        if element != '':
            total_words += 1
    return total_words

def adjust_date(day, month, year):
    return f"{adjust_digits(day)}-{adjust_digits(month)}-{year}"

# Function to show double-digits for days and months
def adjust_digits(date):
    if len(f'{date}') == 1:
        return f'0{date}'
    else:
        return f'{date}'

def create_row(numbering, entry, chilean_date):
    return ["Entry "+str(numbering), entry.__repr__(), chilean_date, entry.category]

def is_noun(text):
    if count_words(text) == 2 and text[:3] in ARTICLES:
        return True
            