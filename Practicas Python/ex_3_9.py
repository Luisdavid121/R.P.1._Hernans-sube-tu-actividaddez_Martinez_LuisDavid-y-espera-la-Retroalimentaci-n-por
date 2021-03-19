#Ecuacion de primer grado

a = int(input('Ingrese el termino a: '))
b = int(input('Ingrese el termino b: '))

if a == 0 and b != 0:
    print('No tiene solucion.')
elif a >=0:
    print('La solucion es x=-',b,'/',a)
if a == 0 and b == 0:
    print('Existen infinitas soluciones')