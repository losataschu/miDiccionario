# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:50:54 2025

@author: losat
"""

import formatting_module as fm

class VocabularyList:
    def __init__(self, vocab_list):
        self.vocab_list = vocab_list
        self.table = self.create_table()
    
# Create the tabla using the entries in the the dictionary
    def create_table(self):
        numbering = []
        vocabulary = []
        i = 1
        entry_i = "Entry "
        for entry in self.vocab_list:
            numbering.append(entry_i + str(i))
            # TODO: add something to deal with wrong entries
            day = fm.adjust_digits(entry.date[0])
            month = fm.adjust_digits(entry.date[1])
            show_date = day+'-'+month+f'-{entry.date[2]}'
            list_row = [entry.__repr__(), show_date, entry.category]
            vocabulary.append(list_row)
            i += 1
        return vocabulary, numbering, ["", "Text", "Date", "Category"]

# Function to show a well-ordered table with my vocabulary   
    def show_table(self, vocabulary, enumeration, columns):
        # TODO: here, I have to complete the function specifying the desired format
        print("{:<10} {:<40} {:<12} {:<12}".format(*columns))
        # TODO: here handle with the case that enumeration and vocabulary have different lengths
        for i in range(len(vocabulary)):
            print("{:<10} {:<40} {:<12} {:<12}".format(enumeration[i], *vocabulary[i]))
            