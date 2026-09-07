def mayor_edad(edad):
   return edad >= 18 
   
   
#Fuera de la funcion
usuario_edad = int(input("ingrese la edad: "))
resultado_edad_usuario = mayor_edad(usuario_edad)

if resultado_edad_usuario:
   print(f"Tienes {usuario_edad}, ya eres mayor de edad")
else:
   print(f"Tienes {usuario_edad}, aun no tienes la mayoria de edad")