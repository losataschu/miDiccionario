
import json
import EntryFormatModule as entryfmt

# Codigo Clase Diccionario
class Dictionary:
    def __init__(self, file_path):
        self.file_path = file_path
        self.all_entries = self.create_entry_list()

    def create_entry_list(self):
        with open(self.file_path, 'r') as file:
            my_entries = json.loads(file.read())
        entry_list_categorized = []
        for entry in my_entries["Entradas"]:
            #print(entrada["palabra"])
            new_entry = entryfmt.build_entry(entry["palabra"], entry["fecha"])
            if new_entry:
                entry_list_categorized.append(new_entry)
        return entry_list_categorized

