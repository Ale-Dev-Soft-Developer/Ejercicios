def es_par(numero1):
   return numero1 % 2 == 0 

numero_usuario = int(input("Ingresa un numero: "))
resultado = es_par(numero_usuario)

if resultado:
   print(f" {numero_usuario} Si es es par ")
else:
   print(f"{numero_usuario} No es par")




