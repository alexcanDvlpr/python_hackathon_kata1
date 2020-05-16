

precio = 3.49
descuento = 1 - 0.6
precioDescuento = precio * descuento

barras = input('Introduce el numero de barras: \n')

print('Precio habitual ' + str(precio))
print('Descuento ' + str(precioDescuento))
print('Precio por Barras ' + str(int(barras) * precioDescuento))