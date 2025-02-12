# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:50:54 2025

@author: losat
"""

from tabulate import tabulate

class VocabularyEntries:
    def __init__(self, vocab_entries):
        self.vocab_entries = vocab_entries
    
# Create the table using the entries in the the dictionary
    def create_formatted_table(self):
        entry_numbering = []
        vocabulary = []
        row = []
        i = 1
        entry_i = "Entry "
        for entry in self.vocab_entries:
            entry_numbering.append(entry_i + str(i))
            # TODO: add something to deal with wrong entries
            adjusted_date = adjust_date(entry.date[0], entry.date[1], entry.date[2])
            row.append(create_row(i, entry, adjusted_date))
            vocabulary.append([entry.__repr__(), adjusted_date, entry.category])
            i += 1
        # return entry_numbering, vocabulary, ["", "Text", "Date", "Category"]
        return row, ["", "Text", "Date", "Category"]

# Function to show a well-ordered table with my vocabulary   
    def show_table(self, enumeration, vocabulary, column_names):
        # print(tabulate([column_names, ["t1","t2","t3","t4"]], headers="firstrow"))
        # TODO: here, I have to complete the function specifying the desired format
        print("{:<10} {:<40} {:<12} {:<12}".format(*column_names))
        # TODO: here handle with the case that enumeration and vocabulary have different lengths
        for i in range(len(vocabulary)):
            print("{:<10} {:<40} {:<12} {:<12}".format(enumeration[i], *vocabulary[i]))

# Function to show a well-ordered table with my vocabulary   
    def show_table_tabulate(self, rows, column_names):
        # print(tabulate([column_names, ["t1","t2","t3","t4"]], headers="firstrow"))
        print(tabulate(rows, headers=column_names))
        # TODO: here, I have to complete the function specifying the desired format
        # print("{:<10} {:<40} {:<12} {:<12}".format(*column_names))
        # TODO: here handle with the case that enumeration and vocabulary have different lengths
        # for i in range(len(vocabulary)):
            # print("{:<10} {:<40} {:<12} {:<12}".format(enumeration[i], *vocabulary[i]))

def count_words(text):
    if len(text) == 0:
        return 0
    words = 1
    for letter in text:
        if letter == ' ' and text[0] != letter and text[-1] != letter:
            words += 1
    return words

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
    if count_words(text) == 2:
        return True
            