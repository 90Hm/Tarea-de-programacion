def calcular_descuento(monto_total, porc_descuento=10): # porc_descuento es un parámetro opcional que representa el porcentaje de descuento (por defecto es 10%)
# Esta funcion calcula el descuento como el monto total multiplicado por el porcentaje de descuento, dividido por 100
    descuento = monto_total * porc_descuento / 100
    return descuento

# Llamadas a la función
valor = calcular_descuento(150.50)  # Calcula el descuento para una compra de $150.50 con el descuento predeterminado del 10%
print("Descuento=", valor)

total_compra = 250.75
desc = 15
valor = calcular_descuento(total_compra, desc)  # Esta funcion calcula el descuento para una compra de $250.75 con un descuento del 15%
print("Total de la compra:", total_compra,
      "Descuento del:", desc,
      "% Descuento=", valor)
