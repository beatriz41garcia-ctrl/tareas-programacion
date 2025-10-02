#1 investigar como se usa el operador modulo(modulus) en phyton, explicando con sus palabras y por un ejemplo
# al simbolo % se le conoce como operador de modulo 
# se usa para obtener el residuo de un problema de división.
print(20%5)
#el residuo es 0
print(56%9)
# en este el residuo es 2

#2 crea una lista vacia y llenala con los numeros pares del 2 al 50 (2,4,6,8,,,,,48,50) utilizando un for y un condicional para controlar que solo los pares se agreguen.
pares=[]
for i in range(2,51):
    if i % 2 ==0:
        pares.append(i)
print("\numeros pares del 2 al 50:")
print(pares)


#3 investigar para que sirve el comando "break" en un for, explicarlo con sus palabras y dar un ejemplo.
#se usa para que nos indicarle donde debe detenerse inmediatamente.
numeros=[1,2,3,4,5,6,7,8,9,10]
for numero in numeros: 
    print(f"procesando el numero:{numero}")
    if numero ==8:
        print("se ha encontrado el numero 8.¡saliendo del bucle!")
        break #sale del bucle'for' inmediatamente
    print(f"este mensaje no se imprimira si el numero es 5")
    print("el bucle ah terminado")

#4 programar el metodo find de los strings a mano sugerencia: utilizar break cuando encuentren lo que buscan
#palabra= 'banana'
#regresar a la posicion de la primera 'a'.
palabra= 'banana'
posicion=-1
for i in range(len(palabra)):
    if palabra[i]=='a':
        posicion=i
        break
    print("\nLa primera 'a' en 'banana' esta en la posicion:",posicion)
# otro ejemplo,
palabra="guitarra"
posicion=4
for i in range(len(palabra)):
    if palabra[i]=="a":
        posicion=i
        break
    print("la primera 'a' en 'guitarra' esta en la posicion:",posicion)

#5 imprimir todos los numeros de la siguiente lista utilizando ciclos
lista=[[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]
for sublista in lista:
    for num in sublista:
        print("#",num)