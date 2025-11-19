#Dado el archivo fasta, hacer un programa con las siguientes funcioens 
# >chr 1 AAAAATGTTTT AAAAAAAAAAA 
# >chr 2 GGGGGGGGGGG ATGCCCCCCCC AAAAAACCCCC atgCCCCCCCC 

# 1. Para todos los encabezados, lo imprima en el formato 
# "Organismo <el nombre del fasta>, contig <el contenido del encabezado, sin el ">""
import re
nombre_archivo = "focas.fasta" 
nombre_archivo_disco = "focas.fasta.txt" 
contenido_fasta = ""
with open(nombre_archivo_disco, 'r', encoding='utf-8') as archivo:
        contenido_fasta = archivo.read()

#2-Para cada línea de secuencia genómica, imprima su contenido de GC en el formato "GC línea <número de línea>: <GC"
def calcular_gc(secuencia):
    secuencia = secuencia.upper()
    total_bases = len(secuencia)
    if total_bases == 0:
        return 0.0
    conteo_gc = secuencia.count('G') + secuencia.count('C')
    return round(conteo_gc / total_bases, 2)

def complemento_reverso(secuencia):
    traduccion_tabla = str.maketrans('ATGCatgc', 'TACGtacg')
    complemento = secuencia.translate(traduccion_tabla)
    reverso_complemento = complemento[::-1]
    return reverso_complemento.upper()


todas_las_secuencias = []
linea_actual = 1
secuencia_actual = ""
es_primera_linea_secuencia = True
for linea in contenido_fasta.strip().split('\n'):
    
    if linea.startswith('>'):
        encabezado = linea[1:].strip()
        print(f"Organismo {nombre_archivo.split('.')[0]}, contig {encabezado}")
        es_primera_linea_secuencia = True
        
    elif linea.strip():
        secuencia_linea = linea.strip()
        
       #2. Imprimir contenido de GC por línea
        gc_linea = calcular_gc(secuencia_linea)
        print(f"GC línea {linea_actual}: {gc_linea}")
        
        #3. Imprimir secuencia complementaria para la primera línea de cada segmento
        if es_primera_linea_secuencia:
            complemento = complemento_reverso(secuencia_linea)
            print(complemento)
            es_primera_linea_secuencia = False
            
        #4-Imprima el número de línea donde encuentre el codón "ATG" en el formato "ATG en línea <número de línea>"
        if re.search("ATG", secuencia_linea, re.IGNORECASE):
            print(f"ATG en línea {linea_actual}")

        
        todas_las_secuencias.append(secuencia_linea)
        linea_actual += 1

# 5. Cálculo del Contenido GC total
secuencia_completa = "".join(todas_las_secuencias)
gc_total = calcular_gc(secuencia_completa)
print(f"GC total del archivo: {gc_total}")
