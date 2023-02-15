x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))
if x == y and y == z:
    print('Triunghiul este echilateral')
elif (x == y  and (x, y)  != z) or (x == z and (x, z) != y) or (y == z and (y,z) != x):
       print('Triunghiul este isoscel')
elif x != y and y != z and z != x:
    print('Este un triunghi oarecare')