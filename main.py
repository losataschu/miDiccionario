# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:00:32 2025

@author: losat
"""

import DictionaryCore as dcore
import FilterSortModule as filt
import FileEditorModule as filedt

def main():
    new_dict = dcore.Dictionary("entradas_reducidas.json")
    my_entries = new_dict.all_entries
    # print(my_entries)
    filt.create_print_entry_table(my_entries)
    new_dict.setup_filtering()
    filt.filter_entries(new_dict, "category", "jijiji")
    filt.filter_entries(new_dict, "initial_letter", "z")
    filt.filter_entries(new_dict, "year", 2023)
    filt.filter_entries(new_dict, "corneta", 20)
    filt.filter_entries(new_dict, "month", 3)
    filt.filter_entries(new_dict, "monthly", [10, 6])
    filt.filter_entries(new_dict, "date", [21, 12, 2023])

    mi_dict2 = dcore.Dictionary("entrada_simple.json")
    my_entries2 = mi_dict2.all_entries
    mi_dict2.setup_filtering()
    print(my_entries2)
    print(mi_dict2.indexed_entries)
    filedt.add_entry(mi_dict2, "bestellen", 14, 1, 2025)
    print(my_entries2)
    print(mi_dict2.indexed_entries)
    filedt.save_entries_to_file(my_entries2, "entrada_simple.json")
    filedt.delete_entry(mi_dict2, "jaja")
    filedt.delete_entry(mi_dict2, "bestellen")
    filedt.save_entries_to_file(my_entries2, "entrada_simple.json")
    print(my_entries2)
    print(mi_dict2.indexed_entries)
    filt.sort_entries(my_entries, "alphabetical")
    # k2 = sorted(my_entries, key=lambda x: x.date[0])
    # filt.list_entries(k2)
    # k2.sort(key=lambda x: x.date[1])
    # filt.list_entries(k2)
    # k2.sort(key=lambda x: x.date[2])
    # filt.list_entries(k2)
    filt.sort_entries(my_entries, "oldest")
    # k3 = sorted(my_entries, key=lambda x: (x.date[2], x.date[1], x.date[0]), reverse=True)
    # filt.list_entries(k3)
    mi_dict2.setup_filtering()
    print(mi_dict2.indexed_entries)


if __name__ == "__main__":
    main()
