# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:38:46 2025

@author: losat
"""

import unittest
import json
import os
# from pathlib import Path
import DictionaryCore as dcore
import FormatDisplayModule as fdm
import FilterSortModule as fsm
import FileEditorModule as fem
import ValidatingModule as vm

class TestCalc(unittest.TestCase):
    
    #TODO: add test methods for sort function.
    
    @classmethod
    def setUpClass(cls):
        no_entry_dict = {"Entradas" : []}
        with open("entradas_testeo.json", "w") as file_new:   
            json.dump(no_entry_dict, file_new)
    
    @classmethod
    def tearDownClass(cls):
        # pass
        #TODO: borrar archivo creado
        if os.path.exists("entradas_testeo.json"):
        # files = os.listdir("miDiccionario")
        # for file in files:
            # if Path(file).name == "testeo":
            os.remove("entradas_testeo.json")
    
    def setUp(self):
        # print("Set up")
        self.entry1 = dcore.build_entry("das Bier", [22, 1, 2025])
        self.entry2 = dcore.build_entry("mitempfinden", [22, 1, 2025])
        self.entry3 = dcore.build_entry("mein Versehen", [22, 1, 2025])
        self.simple_dict = dcore.Dictionary("entrada_simple.json")
        self.entry_list = self.simple_dict.all_entries
        
    def tearDown(self):
        pass

    def test_build_entry(self):
        self.assertIsInstance(self.entry1, dcore.Noun)
        self.assertIsInstance(self.entry1, dcore.Entry)
        self.assertIsInstance(self.entry2, dcore.Entry)
        self.assertIsInstance(self.entry3, dcore.Entry)
    
    def test_count_words(self):
        self.assertEqual(fdm.count_words("das Bier"), 2)
        self.assertEqual(fdm.count_words(""), 0)
        self.assertEqual(fdm.count_words(" mitempfinden"), 1)
        self.assertEqual(fdm.count_words("mit meinem Gewissen "), 3)

    def test_adjust_date(self):
        self.assertEqual(fdm.adjust_date(3, 5, 2021), "03-05-2021")
        self.assertEqual(fdm.adjust_date(21, 7, 2024), "21-07-2024")
        self.assertEqual(fdm.adjust_date(9, 11, 2023), "09-11-2023")

    def test_filter_attribute(self):
        # INCOMPLETE
        self.simple_dict.setup_filtering()
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "month", 11)
        self.assertEqual(len(filtered_list), 1)
        self.assertEqual(filtered_list[0].date[1], 11)
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "month", 3)
        self.assertEqual(len(filtered_list), 0)
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "category", "Noun")
        self.assertEqual(len(filtered_list), 0)
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "category", "Other")
        self.assertEqual(len(filtered_list), 2)
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "day", 29)
        self.assertEqual(len(filtered_list), 1)
        self.assertEqual(filtered_list[0].date[0], 29)
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "day", 30)
        self.assertEqual(len(filtered_list), 0)
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "initial_letter", "d")
        self.assertEqual(len(filtered_list), 1)
        self.assertEqual(filtered_list[0].text[0], "d")
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "initial_letter", "h")
        self.assertEqual(len(filtered_list), 0)
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "year", 2022)
        self.assertEqual(len(filtered_list), 2)
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "year", 2024)
        self.assertEqual(len(filtered_list), 0)
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "monthly", [12,12])
        self.assertEqual(len(filtered_list), 1)
        self.assertEqual(filtered_list[0].date[0], 12)
        self.assertEqual(filtered_list[0].date[1], 12)
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "monthly", [20,2])
        self.assertEqual(len(filtered_list), 0)
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "date", [12,12,2022])
        self.assertEqual(len(filtered_list), 1)
        self.assertEqual(filtered_list[0].date, [12,12,2022])
        filtered_list = fsm.filter_by_attribute(self.simple_dict.indexed_entries, "date", [12,12,2023])
        self.assertEqual(len(filtered_list), 0)
    
    def test_add_entry(self):
        initial_size = len(self.simple_dict.all_entries)
        fem.add_entry(self.simple_dict, "jemandem sein Wort geben", 22, 1, 2025)
        self.assertEqual(len(self.simple_dict.all_entries), initial_size + 1)
        self.assertRaises(ValueError, fem.check_existing_entry, self.simple_dict.all_entries,
                          "durchsetzen")
                          
    def test_delete_entry(self):
        initial_size = len(self.entry_list)
        fem.delete_entry(self.simple_dict, "abarbeiten")
        self.assertEqual(len(self.entry_list), initial_size - 1)

    def test_validating_module(self):
        with self.assertRaises(ValueError):
            vm.validate_category("context")
            vm.validate_init_letter("AB")
            vm.validate_date_number(0)
            vm.validate_date_number(-1)
            vm.validate_month_tuple(23)
            vm.validate_month_tuple([23])
            vm.validate_month_tuple([23, -5])
            vm.validate_month_tuple([0, 5])
            vm.validate_date_list([0, 5])
            vm.validate_date_list([0, 5, 0])

    def test_validate_entry(self):
        # TODO: write this in a better fashion.
        entries = [self.entry1, self.entry2, self.entry3]
        self.assertEqual(vm.validate_entry(entries, "das Bier"), True)
        self.assertEqual(vm.validate_entry(entries, "mitempfinden"), True)
        self.assertEqual(vm.validate_entry(entries, "mein Versehen"), True)
        self.assertEqual(vm.validate_entry(entries, "mein Vers"), None)
    
    def test_saving_file(self):
        new_dict2 = dcore.Dictionary("entradas_testeo.json")
        entries = [self.entry1, self.entry2, self.entry3]
        for entry in entries:
            fem.add_entry(new_dict2, entry.__repr__(), entry.date[0], entry.date[1],
                          entry.date[2])
        fem.save_entries_to_file(new_dict2, "entradas_testeo.json")
        new_dict = dcore.Dictionary("entradas_testeo.json")
        self.assertEqual(len(new_dict.all_entries), len(entries))

if __name__ == "__main__":
    unittest.main()