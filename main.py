import random

print('Esto es el piedra, papel, tijera')

elecciones = ['Piedra', 'Papel', 'Tijera']

eleccion = input('¿Cual es tu eleccion?\n')
eleccionAI = random.choice(elecciones)

print(eleccion)
print(eleccionAI)