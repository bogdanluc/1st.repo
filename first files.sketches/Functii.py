def printGreeting():
    print('Buna ziua!')

def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')

# zona de apelare

printGreeting()
printGreeting()

printGreetingByName('Bogdan', "Lucaciu")

def mediaNr(a, b, c):
    return (a+b+c)/3
print(mediaNr(5,7,2))

def piValue():
    return 3.14
print(piValue())

# exercitiu:
#verificare varsta

def verificaVarsta(varsta):
    if varsta >= 18:
        return True
    else:
        return False

print(verificaVarsta((19)))

age = int(input("Varsta este:"))
if verificaVarsta(age):
    print("cont creat")
else:
    print("fuck off")
