
import json
import FormatDisplayModule as fdm
import FilterSortModule as fsm

class Entry:
    def __init__(self, text, date, category):
        self.text = text
        self.date = date
        self.category = category
    def __str__(self):
        return self.text
    def __repr__(self):
        return self.text

class Noun(Entry):
    def __init__(self, article, text, date, category):
        super().__init__(text, date, category)
        # Un sustantivo se diferencia de una instancia general de la clase Entry
        # por contar con un articulo antes.
        self.article = article
    def __repr__(self):
        return f"{self.article} {self.text}"

# Codigo Clase Diccionario
class Dictionary:
    def __init__(self, file_path):
        self.file_path = file_path
        self.all_entries = self.create_entry_list()
        self.indexed_entries = None

    def create_entry_list(self):
        my_entries = load_entries(self.file_path)
        entry_list_categorized = []
        for entry in my_entries["Entradas"]:
            #print(entrada["palabra"])
            new_entry = build_entry(entry["palabra"], entry["fecha"])
            if new_entry:
                entry_list_categorized.append(new_entry)
        return entry_list_categorized

# function that creates and prints the resulting table
    def show_entry_table(self):
        fsm.create_print_entry_table(self.all_entries)
        
    def setup_filtering(self):
        self.indexed_entries = fsm.index_filter_attributes(self.all_entries)
        if self.indexed_entries:
            print("Available attributes for filtering are:")
            print(", ".join(self.indexed_entries.keys()))

def build_entry(text, date_list):
    entry_to_append = None
    if fdm.is_noun(text):
        noun_parts = text.split(" ", 1)
        entry_to_append = Noun(article=noun_parts[0], text=noun_parts[1],
                               date=date_list, category="Noun")
    else:
        entry_to_append = Entry(text=text, date=date_list,
                                category="Other")
    return entry_to_append

def load_entries(filename):
    with open(filename, 'r') as file:
        return json.loads(file.read())
