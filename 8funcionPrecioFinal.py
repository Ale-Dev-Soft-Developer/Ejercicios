def precio_final(valorNeto):
    return valorNeto * 1.19

valor_producto = int(input("Ingrese el valor del producto: "))
valor_total_producto = precio_final(valor_producto)
print(f"Tu producto sin IVA tiene un costo de {valor_producto}, pero para poder venderlo y pagar el impuesto, tu producto tendría que valer, {valor_total_producto}")