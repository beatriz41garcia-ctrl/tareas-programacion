#1 Crear una lista vacia y llenarla con los números del 1 al 50 (1,2,3,,,,48,49,50)#Usar ciclo
numeros=[]
for i in range(1,49):
 numeros.append(i)
print(numeros)

#2 Crear una lista vacia y llenarla con los números múltiplos de 5 del 2 al 50, hay que usar ciclo
multiplos_de_5=[]
for i in range(2,50):
 if i % 5 ==0:
  multiplos_de_5.append(i)
print(multiplos_de_5)

#3 hacer un programa que imprima * ** *** **** ***** ......
for i in range (1,10):
 print('*'*i)

 #como se usa unn ciclo while y hacer un programa que imprimma los números del 1 al 10 
 #repite acciones indefinidamente hasta que se cumpla o deje de cumplir la condción.
 #CONDICION: UNA EXPRESION QUE PUEDE SER TRUE O FALSE, SI EL CODIGO ES TRUE EL CODIGO DENTRO DEL CICLO SE EJECUTA Y SI ES FALSE EL CICLO TERMINA.

 #EJEMPLO DE TRUE
 i = 1
 while i <=3:
  print(i)
  i+=1
#ejemplo de false
num=-1
while num <=0:
 num=int(input('ingresa un numero positivo'))
