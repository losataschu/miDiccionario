
import EntryFormatModule as entryfmt
import EntryFileEditor as entryedt

class Entry:
    def __init__(self, text, date, category):
        self.text = text
        self.date = date
        self.category = category
    def __str__(self):
        return self.text
    def __repr__(self):
        return f"{self.text}"

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
        self.all_entries = self.entry_list()

    def entry_list(self):
        my_entries = entryedt.load_entries(self.file_path)
        #print(my_entries["Entradas"])
        entry_list_categorized = []
        for entry in my_entries["Entradas"]:
            #print(entrada["palabra"])
            if entryfmt.is_noun(entry["palabra"]):
                noun_parts = entry["palabra"].split(" ", 1)
                entry_list_categorized.append(
                    Noun(article=noun_parts[0],
                         text=noun_parts[1],
                         date=entry["fecha"],
                         category="Noun")
                )
            else:
                entry_list_categorized.append(Entry(text=entry["palabra"],
                date=entry["fecha"], category="Other"))
        return entry_list_categorized

