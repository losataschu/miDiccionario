
import formatting_module as fm
import editing_module as edm

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
        self.list = self.create_list()

    def create_list(self):
        my_entries = edm.load_entries(self.file_path)
        #print(my_entries["Entradas"])
        entries_categorized = []
        for entry in my_entries["Entradas"]:
            #print(entrada["palabra"])
            if fm.count_words(entry["palabra"]) == 2:
                parts = entry["palabra"].split(" ", 1)
                if len(parts) == 2:
                    entries_categorized.append(
                        Noun(article=parts[0],
                             text=parts[1],
                             date=entry["fecha"],
                             category="Noun")
                    )
            else:
                entries_categorized.append(Entry(text=entry["palabra"],
                date=entry["fecha"], category="Other"))
        return entries_categorized

#def isSustantivo(entrada):
#   if contarPalabras(entrada.texto) == 2:
#     return True

