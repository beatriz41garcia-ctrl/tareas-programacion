#conectores
#1. Construye una lista que funcione como un conjunto (set). Esto es, construye una función a la que le pasas una lista y un elemento que agregar pero sólo lo agregue si no existe dentro de la lista, también hay que hacer una función que agregue valores (si la llave no existe hay que agregarla y si ya existe hay que sobre-escribir su valor).
#lista, conjuntoo (set)
def agregar_set(lista, elemento):
    if elemento not in lista:
        lista.append(elemento)
    else:
        print(f"El elemento '{elemento}' ya está en la lista")
    return lista

#para agregar  valores
def agregar_llave_valor(llaves, valores, llave, valor):
    if llave in llaves:
        # Si la llave existe sobre- escribir su valor
        indice = llaves.index(llave)
        valores[indice] = valor
    else:
        # Si no existe, la agrega junto con el valor
        llaves.append(llave)
        valores.append(valor)
    return llaves, valores

# Ejemplo
lista = []
lista = agregar_set(lista, 9)
lista = agregar_set(lista, 2)
lista = agregar_set(lista, 9)  # repetido
print("Lista tipo SET:", lista)

llaves = []
valores = []
llaves, valores = agregar_llave_valor(llaves, valores, "nombre", "Karen")
llaves, valores = agregar_llave_valor(llaves, valores, "edad", 22)
llaves, valores = agregar_llave_valor(llaves, valores, "edad", 19)  # sobre-escribe
print("Llaves:", llaves)
print("Valores:", valores)
#2. Construye dos listas que funcionen juntas como un diccionario. Por ejemplo, simular el diccionario d = {'uno':1, 'dos':2, 'tercero':3} Utilizando las listas debe poder responder "la llave uno, tiene valor 1" Sugerencia, usar el método index de las listas para buscar la llave y luego el índice para buscar el valor correspondiente.

def obtener_valor(llaves, valores, llave_buscar):
    if llave_buscar in llaves:
        indice = llaves.index(llave_buscar)
        return f"La llave '{llave_buscar}' tiene el valor {valores[indice]}"
    else:
        return f"La llave '{llave_buscar}' NO existe."

# Ejemplo
llaves = ['ocho', 'tres', 'cuatro']
valores = [8, 3, 4]

print(obtener_valor(llaves, valores, 'ocho'))
print(obtener_valor(llaves, valores, 'tres'))
print(obtener_valor(llaves, valores, 'x'))  # no existe

#3. Hacer una función que convierta un string con nucleótidos en la proteína correspondiente. Sugerencia, crea un diccionario del código genético. Nota: los codones de paro comunmente se sustituyen por un asterisco (*). Tener cuidado con qué pasa si la secuencia no tiene una longitud múltiplo de 3.
# Diccionario del código genético (RNA)
codigo_genetico = {
    "AUG": "M", "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "GUU": "V",
    "GUC": "V", "GUA": "V", "GUG": "V", "AUU": "I", "AUC": "I",
    "AUA": "I", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "AGU": "S", "AGC": "S", "CCU": "P", "CCC": "P", "CCA": "P",
    "CCG": "P", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A", "UAU": "Y",
    "UAC": "Y", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "GAU": "D",
    "GAC": "D", "GAA": "E", "GAG": "E", "UGU": "C", "UGC": "C",
    "UGG": "W", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGA": "R", "AGG": "R", "GGU": "G", "GGC": "G", "GGA": "G",
    "GGG": "G", "UAA": "*", "UAG": "*", "UGA": "*"
}

def traducir_proteina(secuencia):
    
    secuencia = secuencia.upper().replace("T", "U")
    
    if len(secuencia) % 3 != 0:
        return "Error:NO es múltiplo de 3."

    proteina = ""
    for i in range(0, len(secuencia), 3):
        codon = secuencia[i:i+3]
        proteina += codigo_genetico.get(codon, "?")  # ? si el codón es desconocido
    return proteina

# Ejemplo
seq = "AUGGCCUUUUGA"
print("Proteína:", traducir_proteina(seq))
