def calcular_iva(valor_neto):
    # total = valor_neto * 1.19 Al multiplicar de manera directa por 1.19 me ahorro guardar una variable
    return valor_neto * 1.19

#Uso
producto_neto = float(input("Ingrese el valor neto del producto: "))
valor_iva = calcular_iva(producto_neto)

print(f"El total a pagar de IVA es de: {valor_iva}")