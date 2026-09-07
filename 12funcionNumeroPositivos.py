def numeros_positivos(num1,num2,num3):
    return num1 >= 0 and num2 >=0 and num3 >= 0

numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))
numero3 = int(input("Ingresa el tercer numero: "))

resultado = numeros_positivos(numero1,numero2,numero3)
print(resultado)

if resultado:
    print(f"{numero1}, {numero2}, {numero3} son números positivos")
else:
    print("Uno de los números que ingresaste no es positivo")