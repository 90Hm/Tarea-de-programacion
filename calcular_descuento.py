def calcular_descuento(monto_total, porc_descuento=10):
    descuento = monto_total * porc_descuento / 100
    return descuento

# Llamadas a la función
valor = calcular_descuento(150.50)  # Primera llamada, solo envío el monto total de la compra
print("Descuento=", valor)

total_compra = 250.75
desc = 15
valor = calcular_descuento(total_compra, desc)  # Segunda llamada, envío tanto el monto total como el porcentaje de descuento
print("Total de la compra:", total_compra,
      "Descuento del:", desc,
      "% Descuento=", valor)
