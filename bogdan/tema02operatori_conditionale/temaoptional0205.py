# 5. X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.

x = int(input('x => '))
y = int(input('y => '))
z = int(input('z => '))
if x+y+z==180 :
    print('Triunghiul este valid')
elif x+y+z <180 or x+y+z>180:
    print('Triunghiul nu este valid')

