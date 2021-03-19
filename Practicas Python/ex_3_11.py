#Cuadrante
ax = int (input('Ingrese el valor de ax:\n'))
ay = int (input('Ingrese el valor de ay:\n'))
bx = int (input('Ingrese el valor de bx:\n'))
by = int (input('Ingrese el valor de by:\n'))
#Formula
m1 = (ax + bx)/2 
m2 = (ay + by)/2
m = (m1),(m2)
print('Los puntos medios son:\n',m)

if m1 > 0 and m2 > 0:
    print('El punto esta en el cuadrante 1.')
elif m1 < 0 and m2 > 0:
    print('El punto esta en el cuadrante 2.')
elif m1 < 0 and m2 < 0:
    print('El punto esta en el cuadrante 3.')
elif m1 > 0 and m2 < 0:
    print('El punto esta en el cuadrante 4.')
if m1 == 0 and m2 == 0:
    print('El punto esta en el origen.')