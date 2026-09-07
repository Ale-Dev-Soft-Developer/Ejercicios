peliculas = ["Avengers", "Avatar", "Star Wars", "Spider Man"]

peliculas[2]= "Jurassic World" #Modifica un elemento
peliculas.append("Bajo el sol de Toscana") #Agrega un elemento a la lista
peliculas.remove("Avengers") #Elimina un elemento a la lista

print(peliculas)

#Una forma de hacerlo con FOR
for i in peliculas:
    print(i)
    
#Otra forma de hacerlo con FOR pero con un rango
for i in range(0,4):
    print(peliculas[i])


#Si lleva [] es lista y sino lleva no es lista.