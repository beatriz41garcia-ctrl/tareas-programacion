#1MiEsDigito
def MiEsDigito(cadena):
    return cadena.isdigit()
print(MiEsDigito("1234"))  
print(MiEsDigito("abcd"))  
print(MiEsDigito("123a"))  
print(MiEsDigito("12a4"))  

#2. MiConteo
#Input: dos strings, el segundo es sólo un caracter
#Output: un entero con el número de veces que aparece el segundo string en el primer string

#ejemplos
def MiConteo(texto, caracter):
    if len(caracter) !=1:
        return 0
    return texto.count(caracter)
print(MiConteo("hola mundo", "o")) 
print(MiConteo("hola mundo", "h"))  
print(MiConteo("hola mundo", " ")) 
print(MiConteo("hola mundo", "r ")) 
print(MiConteo("hola mundo", "!")) 
print(MiConteo("hola mundo", "")) 
print(MiConteo("", "A"))
print('jajaja')
#3.GContent
#Input: un string con una secuencia de ADN
#Output: porcentaje de caracteres que son "G" ó "C"
def GCcontent(secuencia):
    if len(secuencia) == 0:
        return 0
    secuencia = secuencia.upper()
    gc = secuencia.count("G") + secuencia.count("C")
    return gc / len(secuencia)
print(GCcontent("ATGC"))  
print(GCcontent(""))      
print(GCcontent("AAAA"))  
print(GCcontent("ATgc")) 
print(GCcontent("GGCC"))  
   
#4MiSwapCase
#Input: un string
#Output: un string que invierta las mayúsculas y minúsculas
def MiSwapCase(texto):
    nuevo = ""
    for c in texto:
        if c.islower():
            nuevo += c.upper()
        elif c.isupper():
            nuevo += c.lower()
        else:
            nuevo += c
    return nuevo
print(MiSwapCase("Hola Mundo"))   
print(MiSwapCase("Panecillos123"))   
print(MiSwapCase("CApucHIna")) 
#probe conbinaciones de minusculas numeros y mayusculas

#5. MiCapitalize
#input: un string
#Output: un string que tenga la primera letra en mayúsculas
def MiCapitalize(texto):
    if len(texto) == 0:
        return texto
    return texto[0].upper() + texto[1:]
print(MiCapitalize("hola"))    
print(MiCapitalize("Hola"))      
print(MiCapitalize(""))         
print(MiCapitalize("123abc"))   
#probe con texto normal, vacío y comenzando con número.

#6. EsPar
#Input: Un número entero
#Output: Imprime si el número es par o impar, no debe regresar nada
def EsPar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
EsPar(4)  
EsPar(7)  
EsPar(0)
#probe con par, impar y el caso especial de 0.
