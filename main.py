# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:00:32 2025

@author: losat
"""

import Diccionario as Dt
import filter_module as filt
import editing_module as edm

new_dict = Dt.Dictionary("entradas_reducidas.json")
my_entries = new_dict.list
#print(my_entries)
filt.list_entries(my_entries)
filt.filter_entries(my_entries, "category", "jijiji")
# filt.filter_entries(my_entries, "initial_letter", "z")
# filt.filter_entries(my_entries, "year", 2023)
# filt.filter_entries(my_entries, "corneta", 20)
filt.filter_entries(my_entries, "month", 3)
filt.filter_entries(my_entries, "monthly", [10,6])
filt.filter_entries(my_entries, "date", [21,12,2023])

mi_dict2 = Dt.Dictionary("entrada_simple.json")
# print(mi_dict2.list)
#edm.add_entry("entrada_simple.json", "bestellen", 14, 1, 2025)
#edm.delete_entry("entrada_simple.json", "jaja")
# filt.sort_entries(my_entries, "alphabetical")
k2 = sorted(my_entries, key=lambda x: x.date[0])
filt.list_entries(k2)
# k2.sort(key=lambda x: x.date[1])
# filt.list_entries(k2)
# k2.sort(key=lambda x: x.date[2])
# filt.list_entries(k2)
# filt.sort_entries(my_entries, "oldest")
# k3 = sorted(my_entries, key=lambda x: (x.date[2], x.date[1], x.date[0]), reverse=True)
# filt.list_entries(k3)
