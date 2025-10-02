#1como podemos concatenar un número a un string? 
#tenemos que convertirlo a string usando la función str
saludo = 'hola'
print(saludo + str(9))

#2 De que tipo son las variables justifica la respuesta

# A) '1'
#ESTE ES UNA CADENA DE TEXTO O MEJOR DICHO UN STR, APESAR DE SER UN NÚMERO PHYTON LO TOMA COMO SI FUERA UNN TEXTO 
print(type(1))

#B) 1.0
#Este numero es decimal porque representa una fraccion de una unidad.
print(type(1.0))

#C) 1.5 + true
#1.5 es un numero decimal ya que contiene una cantida de fraccion de una unidad, true es para referirse al numero 1 ya que el sistema lo toma asi la suma daria 2.5 ya que se suma el true como = 1
print(1.5+True)

#D) 1.5 + 2.5
#esta operacion es de tipo float ya que las dos son de tipo decimal y se mantiene asi ya que el resultado dara (4.0) y lo toma a decimal
print(type(1.5+ 2.5))

#E) 1 + true
# esta variable es tipo entero puesto que 1 es class int y el true es igual a 1 por lo tanto da como clase entero
print(type(1 + True))

#F) False + true
#esta variable tambien da como resultado de class int ya que false es 0 y true es 1 entonces al sumarlos seria 1 y es entero 
print(type(False + True))

#G) true* 0
#esta variable da clase entero ya que el sistema toma implicitamente el numero 0 como false 
print(type(True* 0))

#3 manipulando la variable (concatenando con los metodos de string), convertirla

#A)  "hola"- "ho14"
#para agregarle o modificarlo a numero las ultimas dos solo modifique el hola por solo ho y agregue un string
hola = 'ho'
print(hola + str(14))

#B)  " hola"- "hola"
# para que podamos remover espacios se ve asi
palabra= ' hola'
#en 'hola'

#C) "hOLA"- "HoLA"
#para modificar algunas letras a mayusculas es necesario .upper para convertirlas en mayusculas
texto = 'hOLA' 
print(texto[0].upper()+texto[1].lower()+texto[2].upper()+texto[3].upper())


#D)"hola"-"Hola"
#aqui solamente se modificaria la primera letra usando .upper
texto = 'hola'
print(texto[0].upper()+ texto[1:])


#4 describir las funciones de los metodos y dar 1 ejemplo
#A) metodo count() se utiliza para contar el numero de veces que un elemento especifico aparece en una lista o secuencia de datos
mi_lista =[1,2,3,5,5,5,5,6,7]
cantidad_de_5 = mi_lista.count('5')
print (mi_lista.count(5))

#B) find() busca la primera ocurrencia de una subcadena dentro de otra cadena y devuelve el indice de esa primera
cadena = 'hola, soy una cadena de ejemplo.'
subcadena = 'cadena'
# aqui es cuando se busca
cadena.find(subcadena)


#C) isdigit() comprueba si todos los caracteres de las cadenas son digitos 
txt = "432456"
x = txt.isdigit()


#D) replace() devuelve una nueva cadena con una
frase = "phyton es un lenguaje de programcion popular. phyotn  es facil de aprender"
nueva_frase = "phyton no es facil de aprender"
frase.replace("python", "javascript")
print(nueva_frase)


#5 que problema tiene declarar estas palabras?
#oracion larga = 'hola mundo'
#A) lo genera como error de sintaxis por contener espacios para esto debemos usar un guion bajo
oracion_larga = 'hola mundo'

#B) palabra = 'hola' 'mundo' 
# al hacer esto phyton hace 
palabra = 'hola' 'mundo'
# no lo marca como error pero lo pondria junto
# para lograr que haya espacio entre las palabras lo mejor seria poner 
palabra = 'hola' '  mundo'

#6 investigar "fstring" :que son, como se usan y un ejemplo 
#es una forma de formatear cadenas en phyton y permite insertar variables de ntro de una cadena de texto 
#ayudan a que el codigo sea mas claro y legible y hacer calculos directamente dentro de una cadena
nombre = "karen"
edad = 18
print(f"hola,mi nombre es {nombre} y tengo {edad} años.")



