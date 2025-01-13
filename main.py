# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:00:32 2025

@author: losat
"""

import Diccionario as Dt
import filter_module as filt

new_dict = Dt.Dictionary("entradas_reducidas.json")
my_entries = new_dict.list
#print(my_entries)
filt.list_entries(my_entries)
filt.filter_entries(my_entries, "category", "jiji")
filt.filter_entries(my_entries, "initial_letter", "z")
filt.filter_entries(my_entries, "year", 2023)
filt.filter_entries(my_entries, "corneta", 20)
filt.filter_entries(my_entries, "year", -2023)
filt.filter_entries(my_entries, "monthly", [4,1])
filt.filter_entries(my_entries, "date", [7,12,2022])