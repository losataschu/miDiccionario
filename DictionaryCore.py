
import json
import FormatDisplayModule as fdm
import FilterSortModule as fsm

class Entry:
    """
    Es una entrada almacenada en el diccionario.
    Atributos:
        text (str): es el texto.
        date (list): la fecha en que se registró la entrada. Tiene formato
        [día, mes, año].
        category (str): la categoría gramatical de la entrada. Por ahora solo
        se especifica si es sustantivo
    """
    def __init__(self, text, date, category):
        self.text = text
        self.date = date
        self.category = category
    def __str__(self):
        return self.text
    def __repr__(self):
        return self.text

class Noun(Entry):
    """
    Un sustantivo se diferencia de una instancia general de la clase Entry
    por contar con un articulo antes.
    Atributo:
        article (str): el artículo asociado al sustantivo (der, die, das)
    """
    def __init__(self, article, text, date, category):
        super().__init__(text, date, category)
        self.article = article
    def __repr__(self):
        return f"{self.article} {self.text}"

# Codigo Clase Diccionario
class Dictionary:
    """
    Gestiona el conjunto de entradas del diccionario almacenadas en un archivo JSON.
    Atributos:
        file_path (str): La ruta al archivo JSON que contiene las entradas del
        diccionario.
        all_entries (list): Lista de todas las entradas cargadas del archivo.
        indexed_entries (dict): Diccionario de entradas indexadas por atributos
        para filtrado.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.all_entries = self.create_entry_list()
        self.indexed_entries = None

    def create_entry_list(self):
        """
        Carga las entradas desde un archivo JSON y las convierte en una lista
        de objetos Entry o Noun.
        
        Retorna:
            list: La lista de entradas creadas a partir de los datos del
            archivo JSON.
        """
        my_entries = load_entries(self.file_path)
        entry_list_categorized = []
        for entry in my_entries["Entradas"]:
            #print(entrada["palabra"])
            new_entry = build_entry(entry["palabra"], entry["fecha"])
            if new_entry:
                entry_list_categorized.append(new_entry)
        return entry_list_categorized

    def show_entry_table(self):
        """
        Muestra una tabla de todas las entradas utilizando funciones del módulo
        FilterSortModule.
        """
        fsm.create_print_entry_table(self.all_entries)
        
    def setup_filtering(self):
        """
        Prepara el diccionario para el filtrado indexando las entradas por
        atributos específicos.
        """
        self.indexed_entries = fsm.index_filter_attributes(self.all_entries)
        if self.indexed_entries:
            print("Available attributes for filtering are:")
            print(", ".join(self.indexed_entries.keys()))

def build_entry(text, date_list):
    """
    Construye una entrada basada en el texto y la fecha proporcionados.

    Argumentos:
        text (str): El texto de la entrada.
        date_list (list): La fecha asociada a la entrada en formato [día, mes, año].
    
    Retorna:
        Entry or Noun: La entrada creada, ya sea como Entry o como Noun si el texto
    comienza con un artículo.
    """
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
    """
    Carga las entradas de un archivo JSON.
    
    Argumento:
        filename (str): El nombre del archivo desde el que se cargan las entradas.
        
    Retorna:
        dict: Un diccionario que contiene las entradas cargadas.
    """
    with open(filename, 'r') as file:
        return json.loads(file.read())
