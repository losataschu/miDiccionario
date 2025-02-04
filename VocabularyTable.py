# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:50:54 2025

@author: losat
"""

import EntryFormatModule as entryfmt

class VocabularyEntries:
    def __init__(self, vocab_entries):
        self.vocab_entries = vocab_entries
    
# Create the table using the entries in the the dictionary
    def create_formatted_table(self):
        entry_numbering = []
        vocabulary = []
        i = 1
        entry_i = "Entry "
        for entry in self.vocab_entries:
            entry_numbering.append(entry_i + str(i))
            # TODO: add something to deal with wrong entries
            day = entryfmt.adjust_digits(entry.date[0])
            month = entryfmt.adjust_digits(entry.date[1])
            adjusted_date = day+'-'+month+f'-{entry.date[2]}'
            list_row = [entry.__repr__(), adjusted_date, entry.category]
            vocabulary.append(list_row)
            i += 1
        return entry_numbering, vocabulary, ["", "Text", "Date", "Category"]

# Function to show a well-ordered table with my vocabulary   
    def show_table(self, enumeration, vocabulary, column_names):
        # TODO: here, I have to complete the function specifying the desired format
        print("{:<10} {:<40} {:<12} {:<12}".format(*column_names))
        # TODO: here handle with the case that enumeration and vocabulary have different lengths
        for i in range(len(vocabulary)):
            print("{:<10} {:<40} {:<12} {:<12}".format(enumeration[i], *vocabulary[i]))
            