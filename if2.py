edad = input('Dime tu edad ')
edad = int(edad)

if edad < 4:
    print('El precio de la entrada es 0€.')
elif edad >= 4 and edad <=18:
    print('El precio de la entrada es 5€')
elif edad > 18:
    print('La entrada cuesta 10€')
