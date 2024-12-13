import json
import pandas as pd

words_test = ['abarbeiten', 'die Wertschöpfung', 'etwas in Worte fassen']

def contarPalabras(texto):
  if len(texto) == 0:
    return 0
  palabras = 1
  for caracter in texto:
    if caracter == ' ' and texto[0] != caracter and texto[-1] != caracter:
      palabras += 1
  return palabras

#Codigo Entrada
class Entrada:
  def __init__(self, texto, fecha, categoria):
    self.texto = texto
    self.fecha = fecha
    self.categoria = categoria
  def __str__(self):
    return self.texto
  def __repr__(self):
    return f"{self.texto}"

#Codigo Sustantivo
class Sustantivo(Entrada):
  def __init__(self, articulo, texto, fecha, categoria):
    super().__init__(texto, fecha, categoria)
    self.articulo = articulo
  def __repr__(self):
    return f"{self.articulo} {self.texto}"

# Codigo Clase Diccionario
class Diccionario:
  def __init__(self, direccion):
    self.direccion = direccion
    self.listado = self.crear_listado()

  def crear_listado(self):
    with open(self.direccion, 'r') as file:
      mis_entradas = json.loads(file.read())
      #print(mis_entradas)
      entradas_con_categoria = []
      for entrada in mis_entradas["Entradas"]:
        #print(entrada["palabra"])
        if contarPalabras(entrada["palabra"]) == 2:
          entradas_con_categoria.append(Sustantivo(articulo=entrada["palabra"][0:3], texto=entrada["palabra"][4:], fecha=entrada["fecha"], categoria="Sustantivo"))
        else:
          entradas_con_categoria.append(Entrada(texto=entrada["palabra"], fecha=entrada["fecha"], categoria="Otra"))
      return entradas_con_categoria

class Tabla:
  def __init__(self, listado):
    self.listado = listado
    
# Crear una tabla ocupando las entradas del diccionario
  def crear_tabla(self):
    enumeracion = []
    coleccion = []
    i = 1
    entrada_i = "Entrada "
    for entrada in self.listado:
      enumeracion.append(entrada_i + str(i))
      # TODO: agregar una excepcion para regular errores
      fecha_legible = f'{entrada.fecha[0]}-{entrada.fecha[1]}-{entrada.fecha[2]}'
      linea = [entrada.__repr__(), fecha_legible, entrada.categoria]
      coleccion.append(linea)
      i += 1
    return coleccion, enumeracion, ["", "Palabra", "Fecha", "Categoria"]

  def mostrar_tabla(self, coleccion, enumeracion, columnas):
      # TODO: acá debo mostrar la tabla con el formato que quiero
      for i in range(2):
          print("{}\t".format(columnas[i+1]), end ="")
      print("\n")

def isSustantivo(entrada):
    if contarPalabras(entrada.texto) == 2:
      return True

# esta es la función que filtrará las tablas y entrega los resultados
# def filtrarTabla(tabla, criterio, valor):
#     match criterio:
#       case "categoria": return filtrarCategoria(tabla, valor)
#       case "letra_inicial": return filtrarLetraInicial(tabla, valor)
#       case _: return "Para tal criterio no hay nada aun"

# def filtrarCategoria(tabla, valor):
#     tabla_filtrada = tabla.copy()
#     match valor:
#       case "Sustantivo" | "Otra": return tabla_filtrada.loc[lambda df: df["Categoria"] == valor, :]
#       case _: return "Categoría inválida."

# def filtrarLetraInicial(tabla, valor):
#     tabla_filtrada = tabla.copy()
#     if len(valor) != 1:
#       return "Ingresar solamente una letra."
#     valor = valor.lower()
#     for i in tabla.loc[:,"Palabra"]:
#       if contarPalabras(i) == 2 and i[4] != valor.capitalize():
#         idx = tabla.index[tabla["Palabra"]==i].tolist()
#         tabla_filtrada = tabla_filtrada.drop(idx)
#       elif contarPalabras(i) == 1 and i[0] != valor:
#         idx = tabla.index[tabla["Palabra"]==i].tolist()
#         tabla_filtrada = tabla_filtrada.drop(idx)
#     return tabla_filtrada

nuevo_diccionario = Diccionario("entradas_reducidas.json")
mis_entradas = nuevo_diccionario.listado
print(mis_entradas)
#print(nuevo_diccionario.listado[0].fecha)
#print(nuevo_diccionario.listado[0].__str__())
#print(nuevo_diccionario.listado[1].__repr__())
#print(nuevo_diccionario.listado[1].articulo)

nueva_tabla = Tabla(mis_entradas)
#print(nueva_tabla.tabla)
tabla_entradas, tabla_enum, tabla_cols = nueva_tabla.crear_tabla()
nueva_tabla.mostrar_tabla(tabla_entradas, tabla_enum, tabla_cols)
#encabezado = tabla_entradas.head(10)
print(tabla_entradas)

for i in range(2):
  print("{}\t".format(tabla_cols[i+1]))

#filtrarTabla(tabla_entradas, "letra_inicial", "F")
