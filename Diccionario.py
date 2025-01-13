import json
import formatting_module as fm

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
        self.article = article
    def __repr__(self):
        return f"{self.article} {self.text}"

# Codigo Clase Diccionario
class Dictionary:
    def __init__(self, file_path):
        self.file_path = file_path
        self.list = self.create_list()

    def create_list(self):
        with open(self.file_path, 'r') as file:
            my_entries = json.loads(file.read())
            #print(mis_entradas)
            entries_categorized = []
            for entry in my_entries["Entradas"]:
                #print(entrada["palabra"])
                if fm.count_words(entry["palabra"]) == 2:
                    entries_categorized.append(Noun(article=entry["palabra"][0:3],
                    text=entry["palabra"][4:], date=entry["fecha"], category="Noun"))
                else:
                    entries_categorized.append(Entry(text=entry["palabra"],
                    date=entry["fecha"], category="Other"))
            return entries_categorized

#def isSustantivo(entrada):
#   if contarPalabras(entrada.texto) == 2:
#     return True

