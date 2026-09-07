mi_lista = [1,2,"Hola,", True] #Ejemplo de lista heterogenea
numeros1 = [1,2,3,4,5] #Ejemplo de lista numerica
numeros2 = [6,7,8,9,10] #Ejemplo de lista numerica

#Operaciones con listas
mi_lista.append(4) #Funcion que agrega un elemento al final de la lista
mi_lista.insert(1, "nueva") #Funcion para insertar o agregar un elemento en una posicion especifica



##Para la lista
lista = ["a","b","c","d","e","f"]

#Imprimir valor con comandos de Index
print(lista[:4]) ##Imprime los valores desde el numero 4 hacia la izquierda
print(lista[4:]) ##Imprime los valores desde el numero 4 hacia la derecha
print(numeros1[0:4])#Impimira todos los valores de la posicion 0 a la 4
print(len(numeros1)) #Funcion para conocer la cantidad de elemento que tiene una lista. (len : length)
print(5 in numeros1) #Funcion para consultar si un elementos se encuentra dentro de la lista. Devuelve un TRUE o FALSE

print(numeros1 + numeros2) #Concatenacion de listas, se unen las dos listas en una sola lista.


# TUPLAS ()
# Son inmutables, no se permiten modificaciones por lo que normalmente se utilizan para almacenar datos que no necesitan modificacion.
ejemplo_de_tupla = (1,2,"Hola",3)
ejemplo_de_tupla[0] = 5 #Dara error ya que las tuplas no permiten modificaciones.
