# ![](../static/icon_python.svg) Python

## Despre trainer

```python
trainer = 'Tavi Popoviciu'
subject = 'Python programming language'
message = "Let's code something!"
```

## Introducere, setup

### Caracteristici

- cod curat
- sintaxa aproapiata limbii engleze
- free (gratuit)
- open source (codul poate fi vazut de oricine)
- o multitudine de librarii pentru development
- limbaj de programare interpretat
- dynamically typed
- object oriented (avem clase, si obiecte)

### Aplicatii

- web / desktop / mobile
- data science
- artificial intelligence
- internet of things
- automatizari

### Despre Python

- [Istorie](https://en.wikipedia.org/wiki/Python_(programming_language))
- scris de [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) în 3 luni
- [PEP8](https://www.python.org/dev/peps/pep-0008/), regulile de sintaxa Python
- [PEP20](https://www.python.org/dev/peps/pep-0020/), niste reguli de design si folozofie

### Versiuni

O istorie a versiunilor gasiti [aici](https://en.wikipedia.org/wiki/History_of_Python#Table_of_versions)

- prototip: 1989, după 3 luni de development
- 0.9 (prima versiune lansată) 1991
- 1.0 (prima versiune stabilă) 1994
- 2.0 (versiunea "veche") 2000
- 3.0 (versiunea "nouă") 2008
- 3.10 (versiunea curentă) 2021
- 4.0? Guido van Rossum spune ca probabil nu va fi niciodata

### De instalat

- [Python](https://www.python.org/downloads/) interpreter
- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/) IDE (Integrated Development Environment)

## Primii pasi in python

### Prima linie de cod

```python
print("Hello world!")
```

### Functia print()

O functie este ca un algoritm, cu un nume, si parametri de intrare si/sau iesire.

Functia [print()](https://docs.python.org/3/library/functions.html#print) afiseaza in consola parametrii dati

```python
print()

print(2)
print(15.3)
print('abc')

o_variabila = 'ceva text'
print(o_variabila)

print(1, 2, 3, 4, 5)
print(1, 2, 3, 4, 5, sep='|')
print(1, 2, 3, 4, 5, sep='|', end='>')
```

### Comentarii

Conform PEP-8, [comentariile](https://www.python.org/dev/peps/pep-0008/#comments) se pot pune in 2 feluri.

```python
# acesta este un comentariu

# acesta este 
# un comentariu
# pe mai multe linii

# print("Hello world!") # nu printeaza Hello world, ca e comentat

print("Hello world!")  # printeaza Hello world

"Un string pus ca valoare in cod nu face cam nimic. E alocata memoria pentru el, si atat."

"""
acesta este
un string de 
mai multe linii, 
practicat mai ales in documentarea codului, 
dar nu numai
"""
```

### Variabile, Tipuri de date

O variabila e un spatiu in memorie, cu un nume, in care se afla o oarecare valoare.

Reguli numire variabile conform [PEP-8](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)

- are nume unic
- numele nu contine caractere speciale, spatii, diacritice, etc
- numele nu incepe cu cifre
- se noteaza snake_case

```python
nume_variabila = "o valoare, de data asta de tip str"
text = "Python syntax highlighting"  # str
intreg = 17  # int
zecimal = 17.37  # float
complex_ = 3 + 17j  # complex
logic = True  # bool
nimic = None  # NoneType
```

### Functia type()

Cu un singur argument, functie [type()](https://docs.python.org/3/library/functions.html#type) ne returneaza tipul unei
variabile

```python
print(type(2))
print(type(12.5))
print(type(True))
print(type("abc"))
un_tip = type(None)
```

### Tipuri de date

Conform [documentatiei](https://docs.python.org/3/library/stdtypes.html), avem mai multe tipuri de date

### Type casting

```python
un_int = int("20")
un_alt_int = int(273.15)
un_float = float("3.14")
```

### Operatori

[Documentatie oficiala](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions)

#### Aritmetici

```python
suma = 5 + 2
diferenta = 5 - 2
produs = 5 * 2
rezultat_impartire = 5 / 2
cat_impartire = 5 // 2
rest_impartire = 5 % 2
putere = 5 ** 2
```

#### De atribuire

```python
a = 10
a += 2  # a = a + 2
a -= 3  # a = a - 3
a *= 2  # ...
a /= 3
a //= 2
a %= 3
a **= 2
```

#### De comparatie

```python
print(2 > 5)  # mai mare
print(2 < 5)  # mai mic
print(2 == 5)  # egal
print(2 <= 5)  # mai mic sau egal
print(2 >= 5)  # mai mare sau egal
print(2 != 5)  # diferit
```

#### Logici

```python
si = True and False  # operatia "si"
sau = True or False  # operatia "sau"
negare = not True  # operatia de negare
```

#### De apartementa

```python
inclus = 'py' in 'python is great'
neinclus = 'py' not in 'python is great'
```

#### Speciali

```python
texte_concatenate = "ceva" + " inca ceva"
text_repetat = "-" * 20
```

### Conversii de date

```python
un_numar = float("1.23")
un_bool = bool("True")
un_intreg = int(3.14)
```

### Functia input()

Conform [documentatiei](https://docs.python.org/3/library/functions.html#input), functia ```input()```() primeste un
parametru, text care va fi pus pe ecran inaintea cursorului de
tastatura. Returneaza valoarea introdusa de utilizator

```python
valoare_de_la_tastatura = input("Introduceti o valoare: ")
print(valoare_de_la_tastatura)
print(type(valoare_de_la_tastatura))
```

### Functia [len()](https://docs.python.org/3/library/functions.html#len)

```python
lungimea_unui_text = len("Hello world!")
```

```python
litere = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']
lungimea_unei_liste = len(litere)
```

## Conditionale

### if

Conform [documentatiei](https://docs.python.org/3/tutorial/controlflow.html#if-statements), ```if``` Ne permite sa
executam cod daca o anumita conditie se indeplineste

#### Exemple

```python
if True:
    print("se va afisa tot timpul.")
    print("se va afisa si asta tot timpul.")
```

```python
ora = 37
if ora > 24:
    print("Ora invalida")
```

```python
a = 13
if a % 2 == 0:
    print("a este numar par")
```

#### else

Optional

```python
# sa se verifice daca a este divizibil cu 2
a = 13
if a % 2 == 0:
    print("a este numar par")
else:
    print("a este numar impar")
```

#### elif

```python
# sa se verifice daca a este >, <, = cu 0
a = 10
if a > 0:
    print("a este mai mare decat 0")
elif a == 0:
    print("a este egal cu 0")
else:
    print("a este mai mic ca 0")
```

```python
# sa se verifice daca vreunul din a, b, c este 0
a = 10
b = 15
c = 0
if a == 0:
    print("a este 0")
elif b == 0:
    print("b este 0")
elif c == 0:
    print("c este 0")
else:
    print("niciun numar nu e 0")
```

### match

[Recent](https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching) (python 3.10), pentru a evita
cod de felul

```python
valoare_de_la_tastatura = input('introduceti o valoare')
if valoare_de_la_tastatura == 'A':
    pass
elif valoare_de_la_tastatura == 'B':
    pass
elif valoare_de_la_tastatura == 'C':
    pass
```

#### Exemplu

A fost adaugat statementul [match](https://peps.python.org/pep-0636/)

```python
valoare_de_la_tastatura = input('introduceti o valoare')
match valoare_de_la_tastatura:
    case 'A':
        pass
    case 'B':
        pass
    case 'C':
        pass
```

### assert

Utilizat majoritar in teste, assert e ca un if, care daca nu se indeplineste conditia, genereaza o exceptie:
AssertionError

```python
assert "abc" == "abc"
assert 1 == 0
```

## Bucle

### [while](https://python-reference.readthedocs.io/en/latest/docs/statements/while.html)

Executam repetat un bloc de cod atat timp cat conditia se indeplineste.

Trebuie sa ne asiguram ca conditia de repetare devine neadevarata pentru a evita o bulca infinita.

```python
a = 10
while a > 0:
    print(a)
    a -= 1
```

### else

Daca am epuizat toate valorile, se va executa si else

```python
a = 10
while a > 0:
    print(a)
    a -= 1
else:
    print("am terminat de iterat") 
```

### continue

continue intrerupe bucla curenta, si sare din nou la verificarea conditiei

```python
a = 10
while a > 0:
    a -= 1
    if a == 4:
        continue
    print(a)
else:
    print("am terminat de iterat") 
```

### break

break iese cu totul din while, fara a mai executa else.

```python
a = 10
while a > 0:
    a -= 1
    if a == 4:
        continue
    if a == 7:
        break
    print(a)
else:
    print("am terminat de iterat") 
```

### [for](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

```python
culori = ['rosu', 'galben', 'albastru']
for culoare in culori:
    print(culoare)
else:
    print("Am terminat de iterat prin culori")
```

<br>
else, continue si break functioneaza pe aceleasi principii ca la while

## List slicing

#### String ca lista de caractere

Poate fi definit ca un text, sau ca un șir de caractere

```python
un_text = 'Hello world!'
acelasi_text = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!'] 
```

| H   | e   | l   | l   | l   | o   |     | w   | o   | r   | l   | d   | !   |
|:----|:----|:----|:----|:----|:----|-----|-----|-----|-----|-----|-----|-----|
| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
| -13 | -12 | -11 | -10 | -9  | -8  | -7  | -6  | -5  | -4  | -3  | -2  | -1  |

#### un_text[pozitie]

```python
un_text = "aceasta este o propozitie"
primul_caracter = un_text[0]
al_4lea_caracter = un_text[3]
ultimul_caracter = un_text[len(un_text) - 1]
tot_ultimul_caracter = un_text[-1]
```

#### un_text[start:stop]

```python
un_text = "aceasta este o propozitie"
primele_5_caractere = un_text[0:5]
fiecare_al_doilea_caracter = un_text[0:len(un_text):2]
```

#### un_text[start:stop:step]

```python
un_text = "aceasta este o propozitie"
un_text_invers = un_text[::-1]
```

#### [Metode](https://docs.python.org/3/library/stdtypes.html#string-methods)

Sunt ca niste functii ajutatoare pe fiecare tip de data.

Se apeleaza cu . dupa o valoare o variabila de tip str.

```python

ceva_text = "O propozitie cu predicat. Care nu incepe cu o prepozitie."
print(ceva_text.upper())
print(ceva_text.lower())
print(ceva_text.capitalize())
print(ceva_text.title())
print(ceva_text.index("pre"))
print(ceva_text.replace("predicat", "subiect"))
```

## Colecții

### list

- indexabila
- mutabila
- permite duplicate

```python
o_lista_goala = []
o_alta_lista_goala = list()
o_lista_cu_numere = [1, 2, 3]
o_lista_dinamically_typed = ['abc', None, 17, False]
```

#### Metode:

```python
o_lista = []
o_lista[0] = 0
o_lista.append(1)  # pentru adaugarea unei valori la sfarsit
o_lista.extend([1, 2, 3])  # pentru extinderea cu un alt iterabil
o_lista.index(2)  # pentru a afla pozitia unei valori
o_lista.count(1)  # pentru a numara aparitiile unei valori
o_lista.sort()  # pentru sortare, cu parametrul optional reverse
o_lista.pop(0)  # pentru a elimina de pe o pozitie
o_lista.remove(2)  # pentru a elimina o valoare
```

### tuple

O tupla e ca o lista imutabila (nemodificabila).

- indexabila
- imutabila
- permite duplicate

```python
o_tupla_goala = ()
o_alta_tupla_goala = tuple()
o_tupla_cu_numere = (1, 2, 3, 7, 2, 2, 4)
o_tupla_dinamically_typed = ('abc', None, 17, False)
tot_o_tupla = 1, 6, "abc"
```

#### Metode

```python
o_tupla = (1, 2, 3)
o_tupla.index(2)  # pentru a afla pozitia unei valori
o_tupla.count(1)  # pentru a numara aparitiile unei valori
```

### dictionary

Un dictionar e o colectie formata din perechi cheie-valoare

```python
un_dictionar_gol = {}
un_alt_dictionar_gol = dict()
un_dicitonar_populat = {'nume': 'Tavi', 'varsta': 35}
nume_utilizator = un_dicitonar_populat['nume']
```

#### Metode

```python
un_dictionar_cu_valori = {'a': 3, 'b': 7}
un_dictionar_cu_valori['a'] = 9
o_valoare_existenta = un_dictionar_cu_valori['a']
o_valoare_posibil_existenta = un_dictionar_cu_valori.get('a')
o_alta_valoare_posibil_existenta = un_dictionar_cu_valori.get('c')
o_valoare_cu_default = un_dictionar_cu_valori.get('c', 13)
un_dictionar_cu_valori.keys()  # intoarce o lista cu cheile dictionarului
un_dictionar_cu_valori.values()  # intoarce o lista cu valorile dictionarului
un_dictionar_cu_valori.pop('a')  # sterge o pereche dupa cheie
un_dictionar_cu_valori.update({'d': 99})  # updateaza dictionarul cu perechile din dictionarul dat ca parametru
un_dictionar_cu_valori.clear()  # goleste dictionarul
```

### [set](https://docs.python.org/3/tutorial/datastructures.html#sets)

O colectie neordonata fara duplicate.

E echivalentul multimii de la matematica.

```python
un_set_gol = set()
un_set_populat = {1, 2, 3}
acelasi_set_de_mai_sus = {2, 1, 3}
```

#### [Metode]()

```python
un_set = set()
un_set.union(set())  # reuniune de 2 multimi
un_set.intersection(set())  # intersectie de 2 multimi
```

### Comparatie

|                   | tuple | list | set | dict                     |
|:------------------|:------|:-----|:----|:-------------------------|
| mutabil           | Nu    | Da   | Da  | Da                       |
| indexabil         | Da    | Da   | Nu  | Nu                       |
| permite duplicate | Da    | Da   | Nu  | Pe valori da, pe chei nu |

## Functii

O functie e un algoritm cu parametri de intrare si parametri de iesire.

Avem nevoie de functii pentru:

- modularizarea codului
- evitarea duplicarii codului

La denumire folosim aceleasi reguli ca pentru variabile, cu specificarea facptului ca o functie si o variabila nu pot
avea acelasi nume.

```python
def numele_functiei():
    pass
```

### Parametri de intrare obligatorii

- sunt obligatorii (daca apelezi functia fara ei, primesti exceptie)
- fiecare valoare va fi data parametrului corespunzator, in ordine

```python
def media_aritmetica(a, b):
    pass


media_aritmetica(2, 3)
media_aritmetica(7, 5)
```

### Parametri de iesire

- orice functie returneaza exact 1 valoare
- implicit, returneaza None
- daca avem nevoie sa returnam mai multe valori, folosim:
    - tuple
    - liste
    - dictionare
    - etc.

```python
def media_aritmetica(a, b):
    return (a + b) / 2


ma = media_aritmetica(7, 3)
```

### Parametri de intrare numiti

Daca nu vrem sa urmam ordinea, putem numi parametrii.

```python
def media_aritmetica(a, b):
    pass


media_aritmetica(a=2, b=3)
media_aritmetica(b=2, a=3)
```

### Oricati parametri obligatorii

- 1 parametru tip lista cu * in fata numelui variabilei
- numit in general args

```python
def media_artimetica(*args):
    return sum(args) / len(args)


print(media_artimetica(1, 2))
print(media_artimetica(1, 2, 3, 4, 5, 6))
```

### Parametri optionali

- au valori implicite
- se noteaza cu parametru='valoare'
- se pun dupa parametri obligatorii

```python
def afisare_elemente(e1, e2, e3, sep='|'):
    return str(e1) + sep + str(e2) + sep + str(e3)


afisare_elemente(1, 2, 3)
afisare_elemente(1, 2, 3, sep="^")
```

### Oricati parametri numiti

- 1 parametru tip dictionar notat cu ** inaintea numelui variabilei
- numit in general kwargs

```python
def afisare_elemente(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])


afisare_elemente(a=1, b=2, alt_parametru=True)
```

### Recursivitatea

Recursivitatea este proprietatea unei functii de a se apela pe sine in implementare.

Avem nevoie sa asiguram o conditie de iesire din bucla de apeluri

In primul rand ne asiguram ca apelam functia cu alti parametri decat cei pe care i-am primit.

```python
def suma_pana_la(numar):
    if numar == 0:
        return 0
    else:
        return numar + suma_pana_la(numar - 1)


print(suma_pana_la(50))
```

### Alte functii din python

#### sum()

[sum()](https://docs.python.org/3/library/functions.html#sum) intoarce suma elementelor unei colectii

```python
suma = sum([1, 2, 3, 4])
print(suma)
```

#### snumerate()

[enumerate()](https://docs.python.org/3/library/functions.html#enumerate) intoarce tupla formata din pozitia si valoarea
unui element dintr-o colectie.

```python
animale = ['elefant', 'broasca', 'tigru']
for index, value in enumerate(animale):
    print(index, value, sep='->')
```

#### abs()

[abs()](https://docs.python.org/3/library/functions.html#abs) intoarce valoarea absoluta a unui parametru

```python
print(abs(-15))
print(abs(12))
```

#### sorted()

[sorted()](https://docs.python.org/3/library/functions.html#sorted) intoarce varianta sortata a unei colectii data ca
parametru

```python
print(sorted([6, 2, 7, 9, 5, 2, 6]))
```

## Clase si obiecte

O clasa e ca un sablon dupa care urmeaza sa functioneze toate obiectele instantiate din ea.

```python
class Produs:
    pass


p1 = Produs()
p2 = Produs()
```

### Proprietati si metode

O clasa contine:

- proprietati (variabile ale clasei)
- metode (functii ale clasei)

Metoda `__init__` este mostenita de la obiectul de baza din Python si se numeste si constructor sau initializer.

`self` este prezent ca primul parametru in toate metodele, si exista pentru a putea referi obiectul curent in interiorul
clasei.

### Exemplu

```python
class Produs:
    def __init__(self):
        self.nume = ''  # proprietate
        self.descriere = ''  # proprietate
        self.pret = 0  # proprietate

    def afisare(self):  # metoda
        print(f'{self.nume} {self.pret}')


un_produs = Produs()
un_produs.nume = 'HP'
un_produs.descriere = 'Pavillion dv5'
un_produs.pret = 899.98
print(un_produs.nume)
un_produs.afisare()
```

### Magic methods

```python

class Produs:
    def __init__(self, nume, pret):  # constructor, sau initializer
        self.nume = nume  # proprietate
        self.descriere = ''  # proprietate
        self.pret = pret  # proprietate

    def __str__(self):  # metoda apelata cand un obiect ia forma de string
        return f'{self.nume} {self.pret}'  # returneaza un string

    def __repr__(self):  # metoda apelata cand un obiect este reprezentat intr-un iterabil
        return str(self.nume)  # returneaza un string, anume inmplementarea lui __str__

    def __len__(self):  # metoda __len__ este apelata cand un obiect este dat ca parametru functiei len() 
        return len(self.nume)  # masurand lungimea unui produs, ii masuram lungimea titlului


p1 = Produs('mere', 12.5)
print(p1)
print([p1, ])
print(len(p1))
```

### Clasa de baza din Python

Magic method-urile sunt mostenite din clasa ```object```.

Scrisa explicit sa nu, mostenirea din ```object``` se intampla in definitia oricarei clase.

```python
class Produs(object):
    pass
```

sau

```python
class Produs:
    pass
```

sunt tot una

### Alte magic metohods

```python
class Produs:
    def __abs__(self):
        pass

    def __lt__(self, other):  # less than
        pass

    def __le__(self, other):  # less than or equal
        pass

    def __gt__(self, other):  # greater than
        pass

    def __ge__(self, other):  # greater than or equal
        pass

    def __float__(self):  # ce forma sa ia cand obiectul e dat ca parametru functiei float
        pass
```

### Mostenire

Mosternirea este abilitatea unei subclase de a mosteni proprietati si metode de la o superclasa

### Mostenire: exemplu

```python
class SuperClasa:
    def __init__(self):
        self.proprietate1 = "valoare string"
        self.proprietate2 = 12

    def __str__(self):
        return f'{self.proprietate1} {self.proprietate2}'

    def metoda1(self):
        pass
```

### Mostenire: exemplu

```python
class SubClasa(SuperClasa):
    def __init__(self):
        super().__init__()  # trebuie sa apelam init pe superclasa
        self.proprietate3 = True

    def metoda1(self):
        print("o alta implementare, fara sa apelam implementarea din superclasa")

    def __str__(self):
        return f'{self.proprietate1} {self.proprietate2} {self.proprietate3}'
```

### Mosternire multipla

In python, putem mosteni din mai multe clase, si practic mostenim tot comportamentul tuturor claselor mostenite.

```python
class SuperClasa1:
    pass


class SuperClasa2:
    pass


class SubClasa(SuperClasa1, SuperClasa2):
    pass
```

## Exceptii

O exceptie e o eroare standard in programare.

Exemple:

- SyntaxError
- IndexError
- TypeError
- ValueError
- KeyError

### Tratarea oricarei exceptii (nerecomandat)

```python
try:  # incearca urmatorul cod care e posibil sa genereze o exceptie
    un_intreg = int("abc")  # cod predispus la exceptie
except:  # daca apare orice exceptie in codul de mai sus, se executa blocul except 
    print('A aparut o eroare!')  # cod pentru afisarea sau tratarea eroorii
```

### Tratarea oricarei exceptii (nerecomandat)

```python
try:  # incearca urmatorul cod care e posibil sa genereze o exceptie
    un_intreg = int("abc")  # cod predispus la exceptie
except Exception:  # daca apare orice exceptie in codul de mai sus, se executa blocul except 
    print('A aparut o eroare!')  # cod pentru afisarea sau tratarea eroorii
```

### Tratarea unei exceptii specifice (recomandat)

```python
try:  # incearca urmatorul cod care e posibil sa genereze o exceptie
    un_intreg = int("abc")  # cod predispus la exceptie
except ValueError:  # daca apare exceptia TypeError in codul de mai sus, se executa blocul except 
    print(
        'A aparut eroarea ValueError, ar trebui citita alta valoare de la tastatura!')  # cod pentru afisarea sau tratarea eroorii
```

### mai multe clauze except

Daca un cod poate genera mai multe exceptii, fiecare poate fi tratata in prorpiul bloc ```except```

```python

try:  # incearca urmatorul cod care e posibil sa genereze o exceptie
    un_intreg = int("abc")  # cod predispus la exceptie
except ValueError:  # daca apare exceptia TypeError in codul de mai sus, se executa blocul except 
    print(
        'A aparut eroarea ValueError, ar trebui citita alta valoare de la tastatura!')  # cod pentru afisarea sau tratarea eroorii
except IndexError:  # daca apare exceptia TypeError in codul de mai sus, se executa blocul except 
    print(
        'A aparut eroarea IndexError, din cauza citirii de pe un index inexistent!')  # cod pentru afisarea sau tratarea eroorii
```

### else

Daca e prezent, blocul ```else``` se executa in caz ca nu a aparut nicio exceptie.

```python
try:
    un_intreg = int("abc")  # cod predispus la exceptie    
except ValueError:
    print(
        'A aparut eroarea TypeError, ar trebui citita alta valoare de la tastatura!')  # cod pentru afisarea sau tratarea eroorii
else:
    print('Nu a aparut nicio exceptie')
```

### finally

Daca e prezent, blocul ```finally``` este executat indiferent de aparitia unei exceptii.

```python
try:
    un_intreg = int("abc")  # cod predispus la exceptie    
except ValueError:
    print(
        'A aparut eroarea TypeError, ar trebui citita alta valoare de la tastatura!')  # cod pentru afisarea sau tratarea eroorii
finally:
    print("Va fi executat dupa try cu except")
```

### raise

Daca dorim sa generam o exceptie, folosim keyword-ul ```raise```

```python
raise IndexError
```

### exceptii custom

```python
class InvalidPriceError(Exception):
    pass


if __name__ == '__main__':
    raise InvalidPriceError
```

## Structuri de date

### Stack

O stiva, sau ```stack``` in python, e o structura de date de tip Last In, First Out (LIFO)

[//]: # (![model functionare stack]&#40;https://www.softwaretestinghelp.com/wp-content/qa/uploads/2019/06/pictorial-representation-of-stack.png&#41;)

```python
stack = [1, 2, 3, 4]

# adding elements to top of stack
stack.append(5)
print(stack)  # Output:[1, 2, 3, 4, 5]
stack.append(6)
print(stack)  # Output:[1, 2, 3, 4, 5, 6]

# removing elements from top of stack
# pop() will remove and return the top element
print(stack.pop())  # Output: 6
print(stack.pop())  # Output: 5

print(stack)  # Output: [1,2,3,4]
```

### Queue

O coada, sau ```queue``` in python, e o structura de dare de tip First In, First Out (FIFO)

```python
from collections import deque

queue = deque([1, 2, 3])
# adds elements to the end of list
queue.append(4)
print(queue)  # Output:deque([1, 2, 3, 4])
queue.append(5)
print(queue)  # Output:deque([1, 2, 3, 4, 5])

# retrieves element from begining of list. (first in  first out.)
print(queue.popleft())  # Output:1
print(queue)  # Output:deque([2, 3, 4, 5])
```

### Graph

Daca vem de simbolizat o harta sau ceva echivalent, putem sa o simbolizam sub forma de graf.

Pentru a simboliza un graph, avem nevoie sa ne definim propriul tip de date sa folosim librarii externe.

### Tree

Daca avem de simbolizat o ierarhie, putem folosi un arbore.

Pentru a simboliza un arbore, avem nevoie sa ne definim propriul tip de date sa folosim librarii externe.

## Testare

Testarea un proces software folosit la identificarea erorilor in programare.

### Bug-uri

- [primul bug](https://www.bbvaopenmind.com/en/technology/innovation/when-computer-bugs-where-real-insects/)
- [o lista cu bug-uri majore](https://en.wikipedia.org/wiki/List_of_software_bugs)
- [o alta lista cu bug-uri populare](https://medium.com/swlh/some-of-the-most-famous-bugs-in-software-history-bb16a2ee3f8e)

### Piramida de testare

![Piramida de testare](https://blog.atinternet.com/wp-content/uploads/2019/12/pyramid-traditional-test-systeme-levels-1.jpg)

```shell
    /\       Acceptance tests
   /  \      System tests
  /    \     Integration tests
 /      \    Unit tests
```

#### Unit tests

Sunt teste menite sa testeze complet functionalitatea unei componente de baza:

- functie
- clasa

Sunt singurele teste scrise de programatori, si nu de testeri. Este cel mai ieftin si mai rapid nivel la care putem
detecta erori

ex:

- daca e gata clasa Product, sau Payment, sau functia conver_f_to_c(), putem sa le testam pe fiecare in parte complet.

#### Integration tests

Testeaza integrarea componentelor/modulelor impreuna.

E al doilea cel mai ieftin si rapid nivel la care putem detecta erori.

ex:

- daca e gata partea de backend si baza de date, se pot testa impreuna, fara frontend

#### System tests

Se numesc si end-to-end tests.

Cand toate componentele/modulele sunt integrate, putem testa intreg sistemul.

E cel mai scump nivel la care putem detecta bug-uri

ex:

- test pentru tot flow-ul de useri: register, login, order, checkout, etc

#### Acceptance tests

E un set special de teste pentru fiecare cerinta specifica a clientului.

ex:

- clientul vrea ca prima pagina sa aibe culoare de background verde #00cc00
- clientul vrea ca link-ul cu termenii si conditiile GDPR sa se deschida intr-o fila noua.

### O unitate pentru test

Fiind dat pachetul cu 2 functii de conversie de temperaturi temperatures.py

```python
def c_to_f(c):
    return c * 5 / 9 + 32
```

### Exemplu: unittest

Inclus in libraria de baza Python.

Folosit doar la unit tests.

```python
import unittest


class TemperatureConverterTests(unittest.TestCase):

    def test_0c_to_f(self):
        c = 0
        f = c_to_f(c)
        # assert folosind operatorul Python
        assert f == 32

    def test_100c_to_f(self):
        c = 100
        f = c_to_f(c)
        # assert folosind operatorul Python
        self.assertEquals(f, 212)
```

### Exemplu: pytest

Instalat de pe pip.

Folosit la unit tests, si nu numai.

```shell
pip install pytest
```

```python
import pytest


def test_0c_to_f(self):
    c = 0
    f = c_to_f(c)
    assert f == 32


def test_100c_to_f(self):
    c = 100
    f = c_to_f(c)
    assert f == 212
```

### Selenium

Selenium este o librarie cu ajutorul careia putem controla un browser direct din cod de python.

Instalat de pe pip.

Folosit la integration sau system tests, avand nevoie de componenta web functionala.

```shell
pip install selenium
```

Downloadam driverul pentru browserul dorit, si il copiem in acelasi folder cu scriptul de python.

- [Chrome](https://sites.google.com/chromium.org/driver/)
- [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- [Firefox](https://github.com/mozilla/geckodriver/releases)
- [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

### Exemplu: selenium

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")  # cu metoda get incarcam un url
assert "Python" in driver.title  # confirmam ca am ajuns pe pagina buna
elem = driver.find_element(By.NAME, "q")  # cautam casuta de search in pagina
elem.clear()  # curatam continutul casutei
elem.send_keys("pycon")  # scriem textul pyton
elem.send_keys(Keys.RETURN)  # apasam ENTER pe casuta
assert "No results found." not in driver.page_source  # confirmam ca avem rezultate
driver.close()  # inchidem fereastra de browser
```

### Search by ID

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")  # cu metoda get incarcam un url
elem = driver.find_element(By.ID, "q")  # cautam casuta de search in pagina
```

### Selectori

#### By.ID

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.find_element(By.ID, 'first_name')
driver.find_elements(By.ID, '')
```

## Iteratori, generatori

### Iteratori

E un mecanism prin care putem lua elemente unul cate unul dintr-un iterabil.

```python
fructe = ("apple", "banana", "cherry")

iterator_fructe = iter(fructe)
print(next(iterator_fructe))
print(next(iterator_fructe))
print(next(iterator_fructe))
```

### Iterator: clasa

```python
class NumberIterator:
    def __init__(self, start=0):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        temp = self.current
        self.current += 1
        return temp


iterator_numere = NumberIterator()
un_iterator = iter(iterator_numere)
print(next(un_iterator))
print(next(un_iterator))
print(next(un_iterator))
```

### Functii generatoare

O functie generatoare e un mod de a reprezenta un iterabil.

In loc sa contina 1 return, va contine mai multe yield-uri.

Yield e ca un return partial, care permite continuarea executiei functiei pana la urmatorul yield.

```python
def numbers(from_, to):
    for number in range(from_, to + 1):
        yield number


my_numbers = numbers(1, 100)
print(my_numbers)
print(list(my_numbers))
```

### Functii generatoare

Avantaje:

- viteza mult mai mare
- eficient alocat in memorie, fiind alocata memoria doar pentru un singur obiect o data
- Posibilitatea de a reprezenta un iterabil infinit
- Posibilitatea obtinerii de valori cum sunt generate

## Fisiere

### Functia open()

Python supporta citire si scriere de fisiere text si binare cu ajutorul
functiei [open()](https://docs.python.org/3/library/functions.html#open)

Primul parametru este obligatoriu, si reprezinta numele fisierului relativ la folderul curent.

Al doilea parametru e optional, si reprezinta modul de deschidere (citire/scriere), si formatul (text/binar)

```python
file = open('file.txt')  # mod read text implicit
file.close()  # fisierul trebuie inchis dupa efectuarea tuturor operatiilor
```

Cu ajutorul unui context manager, fisierul se inchide automat la iesirea din block-ul with.

```python
with open('file.txt', 'rt') as file:  # mod read text explicit
    pass
```

### Citire si scriere text

- Scriere

```python
with open('file.txt', 'wt') as file:  # mod write text
    file.write('un text')  # scrie un anumit text in fisier
```

- Citire

```python
with open('file.txt', 'rt') as file:  # mod citire text explicit
    lines = file.readlines()  # intoarce o lista cu toate liniile din fisier
    print(lines)
```

### pickle

Libraria pickle stie sa:

- scrie 1 obiect in 1 fisier
- citeasca 1 obiect din 1 fisier

- Scriere

```python
import pickle

object_to_save = {'cheie': 'valoare'}
with open('obiect.pickle', 'wb') as file:
    pickle.dump(object_to_save, file)  # scrierea efectiva a obiectului in fisier
```

- Citire

```python
import pickle

with open('obiect.pickle', 'rb') as file:
    object_read = pickle.load(file)  # citirea efectiva a obiectului din fisier
    print(object_read)
```

### JSON

Javascript Object Notation, prescurtat [JSON](https://json.org/example.html), este un mod de serializare a unui
obiect.

Seamana foarte mult ca structura cu dictionarul din python.

Folosim doar ghilimele duble pentru texte.

```json
{
  "cart": {
    "status": "open",
    "items": [
      {
        "product_id": 13,
        "quantity": 15
      },
      {
        "product_id": 4,
        "quantity": 2
      }
    ]
  }
}
```

### Libraria json

- Scriere

```python
import json

object_to_write = {'1': 2, 'abc': True}
with open('file.json', 'wt') as file:
    json.dump(object_to_write, file)  # scrierea efectiva a obiectului in fisier
```

- Citire

```python
import json

with open('file.json', 'rt') as file:
    object_read = json.load(file)  # citirea efectiva a obiectului din fisier
    print(object_read)
```

## Advanced classes:

### Abstractizare

#### Metode abstracte

O metoda abstracta e o metoda neimplementata in clasa curenta, menita sa fie implementata in mostenitori.

Pachetul ```abc``` care contine clase si functii legate de abstractizare.

ABC este Abstract Base Class, din care mostenim clasele abstracte.

Orice clasa care contine cel putin 1 metoda abstracta trebuie sa fie abstracta la randul ei.

Dintr-o clasa abstracta nu putem instantia obiecte.

####                                                                                                        

```python
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def afisare(self):
        pass


instanta = AbstractClass()  # arunca exceptie, pentru ca e
```

#### Mostenirea unei clase abstracte

Mostenind clasa abstracta, putem instantia obiecte din noua clasa.

Daca avem metoda implementata, o putem apela

```python
class ClasaMostenita(AbstractClass):
    def __init__(self):
        self.proprietate_str = "abc"

    def afisare(self):
        print(self)

    def __str__(self):
        return f'Prpprietatea este {self.proprietate}'


instanta_valida = ClasaMostenita()
instanta_valida.afisare()
```

#### Interfete

O interfata e o clasa cu toate metodele abstracte.

### Polimorfism

Aceeasi metoda, functionalitate diferita

```python
class Cat:
    def speak(self):
        print("Miau!")


class Dog:
    def speak(self):
        print("Ham Ham!")


animals = [Cat(), Dog()]
for animal in animals:
    animal.speak()
```

### Encapsulare

O proprietate ar trebui accesata prin metodele publice, fara a se expune intregului program.

Pentru ascunderea unei proprietati, folosim urmatoarea sintaxa:

```python
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand  # proprietate publica, se poate accesa de oricine
        self._model = model  # proprietate protected, poate fi accesata de clasa curenta si de mostenitori
        self.__color = color  # proprietate privata( in python mangled property), accesibila doar in clasa curenta


volvo = Car('Volvo', 'XC70', 'grey')
print(volvo.brand)  # cod valid
print(volvo._model)  # warning
print(volvo.__color)  # exceptie
```

Daca o proprietate are nevoie sa fie accesata, se face prin metode accesor.

```python
class Car:
    def __init__(self, brand):
        self.__brand = brand

    @property
    def brand(self):
        print(f'Returning brand...')
        return self.__brand

    @brand.setter
    def brand(self, brand):
        print(f"Setting brand to {brand}...")
        self.__brand = brand

    @brand.deleter
    def brand(self):
        print(f'Deleting brand...')
        del self.__brand


volvo = Car('Volvo')
volvo.brand = 'Mercedes'  # apeleaza setter
print(volvo.brand)  # apeleaza getter
del volvo.brand  # apeleaza deleter
```

### Compozitie

Daca relatiA "este un" o rezolvam prin mostenire, relatia "are un" o rezolvam prin compozitie.

Compozitia denota faptul ca o clasa poate fi compusa din instante ale altor clase (ca proprietati).

```python
class Color:
    def __init__(self, name):
        self.name = name


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color  # composition, deoarece colo e o instanta din Color


volvo = Car('Volvo', Color('red'))
```

### SOLID principles

Denumite si "The SOLID principles of object oriented programming", sunt 5 principii care ne ajuta la design-ul claselor.

#### Single Responsibility Principle

O clasa are o singura responsabilitate.

Daca avem mai multe responsabilitati, creem mai multe clase.

#### Open/Closed Principle

Daca avem o bucata de program care functioneaza cu o clasa existenta Produs, si pentru urmatoarea bucata avem nevoie de
o varianta modificata a clasei, in loc sa modificam in clasa initiala si sa stricam functionalitatea existenta, putem
mosteni clasa initiala, si modifica mostenitorul.

Astfel, vom avea 2 clase:

- cea initiala cu care functioneaza totul pana acum
- cea mostenita, pentru noua parte

#### Liskov substitution principle

Daca substituim clasele cu interfetele lor, codul ar trebui sa fie valid sintactic.

In python, fiind dynamically typed, nu avem ce schimba. Putem eventual verifica ca orice metoda publica e mostenita
dintr-o interfata.

#### Interface segregation principle

Functionalitate diferita are nevoie de interfata diferita. In python, o clasa poate mosteni oricate clase.

#### Dependency inversion principle

Daca avem neoie sa depindem de o clasa, e mai bine sa depindem de o interfata a acesteia.

## Design patterns

Un design pattern e o solutie recomandata la o problema comuna.

### Creational

Tin de instantierea obiectelor

#### Singleton

Daca avem nevoie de o clasa care sa aibe o singura instanta pe tot parcusul aplicatiei, putem implementa un singleton.

```python
class Singleton:
    instance = None  # proprietate statica, adica a clasei, si nu a instantei.

    def __new__(cls, *args, **kwargs):  # cls refera clasa curenta, Singleton, NU o instanta a ei.
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            # lazy init pe o proprietate
            cls.instance.color = 'red'
        return cls.instance


s1 = Singleton()
print(s1)
s1.color = 'yellow'

s2 = Singleton()
print(s2)
print(s2.color)
```

#### Factory

Daca avem nevoie de una sau mai multe instante de obiecte, putem crea un factory method.

```python
class Volvo:
    pass


class Mercedes:
    pass


def CarFactory(brand="Volvo"):
    avaliable = {
        'Volvo': Volvo,
        'Mercedes': Mercedes
    }
    return avaliable[brand]()
```

#### Builder

Daca avem de construit un obiect din multe seturi de parametri de intrare, putem implementa un builder.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.color = self.shade = self.metallic = None

    def with_color(self, color, shade, metallic=True):
        self.color = color
        self.shade = shade
        self.metallic = metallic
        return self

    def with_engine(self, power, torque, displacement):
        # implementation
        return self


volvo = Car("Volvo").with_color("red", "cherry", False).with_engine("150HP", "320Nm", "20L")
print(volvo)
```

### Structural

Tin de structuri de obiecte si functii

#### Decorator

Daca avem nevoie sa executam cod inainte sau dupa executia unei functii (fara a modifica in vreun fel functia), putem
implementa un decorator.

In python, un decorator va decora tot timpul o functie.

##### decorator functie

```python
def decorator_function(function):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        result = function(*args, **kwargs)
        print("ceva dupa")
        return result

    return inner


@decorator_function
def o_functie_oarecare(p1, p2, *args, **kwargs):
    print(p1, p2, args, kwargs)
    return True


val = o_functie_oarecare(2, 5, 7, a=1, b=3)
```

##### decorator clasa

```python
class DecoratorClasa:
    def __init__(self, function):
        self.__function = function

    def __call__(self, *args, **kwargs):
        print("ceva inainte")
        result = self.__function(*args, **kwargs)
        print("ceva dupa")
        return result


@DecoratorClasa
def ceva_functie(p1, p2, *args, **kwargs):
    print(p1, p2, args, kwargs)
    return 'abc'


valoare = ceva_functie(1, 2, 3, 4, 5, a=1, b=2, c=3)
print(valoare)
```

#### Adapter

Daca avem nevoie sa conectam 2 interfete incompatibile, putem implementa un adapter.

```python
class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"
```

####

```python

def client_code(target: "Target") -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
```

### Behavioral

#### Memento

Daca avem nevoie de un snapshot al unei instante, putem sa folosim un memento.

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class DictionaryMemento:
    def __init__(self, un_user):
        self.un_user = un_user
        self.memory = {}
        self.backup()

    def backup(self):
        self.memory['username'] = self.un_user.username
        self.memory['email'] = self.un_user.email

    def restore(self):
        self.un_user.username = self.memory['username']
        self.un_user.email = self.memory['email']
```

####                                    

```python
tavi = User('tavi', 'tavi.popoviciu@yahoo.com')
memento = DictionaryMemento(tavi)
memento.backup()
tavi.email = "tavi.popoviciu@multibit.ro"
memento.restore()
print(tavi.email)
```

#### Iterator

Implementat nativ in python prin functiile iter() si next()

#### Observer

Daca o clasa are nevoie sa primeasca orice noua valoare a unei proprietati ale unei alte clase, putem implementa un
observer-observable.

```python
class Observer:
    def __init__(self):
        pass

    def new_value_received(self, value):
        print(f"Am primit o noua valoare! {value}")


class Observable:
    def __init__(self):
        self.o_proprietate = 17
        self.observers = []

    def set_o_proprietate(self, valoare):
        self.o_proprietate = valoare
        for observer in self.observers:
            observer.new_value_received(self.o_proprietate)

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)
```

####

```python
observer_ = Observer()
observable = Observable()

observable.add_observer(observer_)
observable.set_o_proprietate(23)
observable.set_o_proprietate(74)
observable.remove_observer(observer_)
observable.set_o_proprietate(53)
```

## Algorithms

Sortare
[visualizare grafica](https://www.toptal.com/developers/sorting-algorithms)

Tipuri:

- Bubble Sort
- Insertion Sort
- Merge Sort
- multe altele

### Computational complexity

Complexitatea reprezinta timpul scurs si memoria consumata in timpul executiei unui algoritm.

- Complexitate temporala
- Complexitate spatiala

Daca avem o sortare de facut cu: 10, 100, 1000, etc elemente, cum evolueaza timpul necesar executiei?

Pentru masurarea memoriei consumate avem nevoie de tool-uri specializate.

Masurarea timpului necesar se poate face cu ajutorul unui decorator, sau a modulului timeit.

###

[vizualizare grafica](https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7)

Complexitate de timp:

- O(1) - complexitate constanta, adica timpul ramane acelasi indiferent de numarul de elemente
- O(n) - complexitate liniara, adica pentru fiecare element in plus, avem nevoie de unitate de timp in plus.
- O(2n) - complexitate liniara dubla, adica 1 element = 2 pasi de timp
- O(n<sup>2</sup>) - complexitate patratica
- O(n<sup>3</sup>) - complexitate cubica
- O(a<sup>n</sup>) - complexitate exponentiala
- O(n log n) - complexitate logaritmic liniara
- O(n!) - complexitate factoriala

## Databases

O baza de date e o colectie de date structurata.

- Relationale (optimizate pentru entitati care relationeaza intre ele):
    - MySQL
    - PostgreSQL
    - SQLite
    - Oracle
    - altele

- Non-relationale (optimizate pentru entitati care nu relationeaza intre ele):
    - MongoDB
    - Google Firestore
    - altele

### Base de date relationale: MySQL

SQL = Structured Query Language

MySQL este un SQL cu parti open source de la Microsoft.

Instalati:

- [MySQL server](https://dev.mysql.com/downloads/mysql/)
- [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)

#### Sintaxa

- [Database and table management](https://www.w3schools.com/mySQl/mysql_create_db.asp)
- [SQL syntax](https://www.w3schools.com/mySQl/mysql_sql.asp)

#### pymysql

- [Instalare](https://pymysql.readthedocs.io/en/latest/user/installation.html)
- [Exemple](https://pymysql.readthedocs.io/en/latest/user/examples.html)

### Extra: SQLite 3

Implementeaza un set redus de SQL, care **nu** are nevoie de un server dedicat. Datele sunt persistate intr-un fisier,
si o librarie este suficienta pentru a stoca baza de date.

Instalati:

- [DB Browser](https://sqlitebrowser.org/dl/)

#### python sqlite3

[sqlite3 official documentation](https://docs.python.org/3/library/sqlite3.html)

### Extra: MongoDB

Optimizat pentru entitati care **nu** relationeaza intre ele.

- database = database
- table = collection
- record = document

Orice colectie accepta orice JSON ca document, indiferent de structura/continut.

## HTML, CSS, JS

### HTML

HyperText Markup Language

Versiune curenta: HTML5

#### Tag-uri

```html

<html></html>
```

#### atribute si valori

```html

<html lang="ro"></html>
```

#### html, head, body

```html

<html>
<head>
    <title>Titlul tab-ului</title>
</head>
<body>
Continut
</body>
</html>
```

#### Comentarii

```html
<!--Acesta este un comentariu-->

<!--Acesta este un comentariu
    pe mai multe linii-->
```

#### h1, h2, h3, h4, h5, h6, p

```html
<h1>Titlu 1</h1><!--Cel mai mare titlu-->
<h2>Titlu 2</h2>
<h3>Titlu 3</h3>
<h4>Titlu 4</h4>
<h5>Titlu 5</h5>
<h6>Titlu 6</h6><!--Cel mai mic titlu-->
```

#### paragraf

```html
<p>Acesta este un paragraf.</p>
```

#### input

```html
<input type="text"> `
<input type="password">
<input type="date">
<input type="time">
<input type="radio">
<input type="checkbox">
<input type="color">
<input type="email">
<input type="file">
<input type="hidden">
<input type="number">
<input type="tel">
```

#### select

```html
<select>
    <option value="1">Aceasta este o optiune</option>
    <option value="2">Aceasta este o alta optiune</option>
</select>
```

#### textarea

```html
<textarea>Un text de mai multe randuri</textarea>
```

#### button

```html

<button>Acesta este un buton</button>
```

#### div

div este un container care dispune elementele unul sub altul

```html

<div>
    <h1>Titlu</h1>
    <p>Continut</p>
</div>
```

#### span

Un ```span``` este un container care dispune elementele unul langa altul.

```html
<span>
    <h1>Titlu</h1>
    <p>Continut</p>
</span>
```

#### formulare

```html

<form>
    <input type="text" name="username">
    <input type="password" name="password">
    <button type="submit">Submit</button>
</form>
```

### CSS

Cascading Style Sheets

Creat pentru a stiliza HTML-ul

Versiune curenta: CSS3

[Tutorial w3schools](https://www.w3schools.com/css/css_intro.asp)

### JavaScript

Limbaj de programare folosit pentru munca in interiorul browserului.

Versiune curenta: JavaScript EcmaScript 6 (ES6)

- interpretat de browser
- dynamically typed
- functional paradigm (suporta functii)
- OOP paradigm (suporta clase si obiecte)

[Tutorial w3schools](https://www.w3schools.com/js/js_intro.asp)

###

Utilizari frontend:

- popup-uri
- acces locatie, inclusiv prin GPS
- acces camera pentru foto/video
- acces accelerometre, alti senzori
- generare grafice (plotly, etc)

Incepand din 2009 cu libraria nodeJs, Javascript ruleaza si pe partea de backend.

#### Functii

```javascript
function oFunctie(param1, param2) {
    console.log("Am intrat in oFunctie");
    console.log("Parametri sunt "+param1.toString()+" "+param2.toString());
}
```

## Backend development: Django

Architectura Model-View-Template, care e un Model-View-Controller specific.

Model ⇆ View ⇆ Template

### Setup initial

#### Legenda:

```numele_aplicatiei``` se inlocuieste cu numele efectiv al aplicatiei(products, users, carts, etc)

```numele_proiectului``` se inlocuieste cu numele efectiv al proiectului (django_shoppy, i_shop, etc)

#### Crearea unui proiect

https://docs.djangoproject.com/en/3.2/ref/django-admin/

Deschidem un "cmd" in folderul unde dorim sa creem proiectul.

```shell
django-admin startproject numele_proiectului
```

#### Instalarea dependintelor

Deschidem folderul proiectului (cel care il contine pe ```manage.py```) in PyCharm, si ii creem un nou
Virtual Environment.

Restartam terminalul din PyCharm,si dam comanda

```shell
pip install django
```

Pentru a avea posibilitatea sa adaugam un ```ImageField```, este necesar si editorul de imagini ```pillow```

```shell
pip install pillow
```

### Crearea unei aplicatii

Un proiect contine una sau mai multe aplicatii.

In terminalul din PyCharm, dam comanda:

```shell
python manage.py startapp products
```

Apoi adaugam aplicatia in proiect.

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'products',
]
```

### Django ORM

Object Relational Mapper este o componenta software care realizeaza comunicarea intre

| Programare orientata pe obiecte | Baze de date relationale |
|---------------------------------|--------------------------|
| clasa                           | tabel                    |
| obiect                          | rand                     |
| proprietate a clasei            | coloana                  |
| proprietate a obiectului        | celula                   |

Vom defini cate o clasa pentru fiecare tabel.

Obiectele instantiate din clasele respective vor fi inregistrari in tabelul corespunzător.

#### Definitia modelelor

Clasele (tabelele) vor fi definite in fisierul ```models.py``` al aplicatiei.

Pentru a primi tabel in baza de date, coloana ID (primary key, auto increment), si altele, clasa se mosteneste
din ```models.Model```.

Pentru fiecare coloana a tabelului definim o proprietate a clasei, si toate posibilitatile se afla in
pachetul ```models```.

[Tipuri de field-uri](https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types)

[Optiuni field-uri](https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-options)

#### Exemplu

```python
# products/models.py
class Category(models.Model):
    name = models.CharField(max_length=79)  # varchar
    icon = models.ImageField(upload_to='static/categories/')  # varchar + fisier in folderul statis


class Product(models.Model):
    name = models.CharField(max_length=79)  # varchar
    description = models.TextField()  # text
    price = models.DecimalField(max_digits=10, decimal_places=2)  # decimal
    stock = models.IntegerField()  # int
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)  # int + foreign key + stergi categoria, stergi si produsele
    image = models.ImageField(upload_to='static/products')  # varchar + fisier in folderul statis


class Cart(models.Model):
    CART_STATUSES = (
        ('open', 'Deschis'),
        ('closed', 'Inchis')
    )
    status = models.CharField(max_length=30, choices=CART_STATUSES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
```

#### Integrare Django Admin Panel

Deschidem fisierul ```admin.py``` din aplicatie, si pentru fiecare clasa definita in ```models.py``` adaugam:

```python
# products/admin.py
admin.site.register(NumeleClasei)
```

#### Integrare MySQL

By default, Django vine setat cu SQLite3, care tine toata baza de date intr-un fisier.

Daca dorim sincronizarea cu o baza de date MySQL, schimbam constanta ```DATABASES``` in ```settings.py```

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB_NAME',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```

### Sincronizarea bazei de date cu clasele de model

In cmd dam comenzile

```shell
python manage.py makemigrations
python manage.py migrate
```

Pentru eficienta, putem crea un fisier ```.bat``` pentru Windows, sau ```.sh``` pentru Linux sau Mac OS.
Continutul de mai sus e valabil pentru toate 3 platformele.

### Crearea unui superuser

In terminal, dam comanda:

```shell
python manage.py createsuperuser
```

### Pornirea serverului: In terminal, dam comanda:

```shell
python manage.py runserver
```

Apoi accesam panoul de administrare la [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

### Adaugarea URL-urilor unei aplicatii in proiect:

[Documentatie 1](https://docs.djangoproject.com/en/4.1/ref/urls/)

[Documentatie 2](https://docs.djangoproject.com/en/4.1/topics/http/urls/)

Deschidem folderul aplicatiei, si creem fisierul ```urls.py```, cu urmatorul continut:

```python
urlpatterns = []
```

Deschidem numele_proiectului/urls.py, si adaugam un nou element in lista urlpatterns:

```python
path('numele_aplicatiei/', include('numele_aplicatiei.urls'))
```

### Crearea unei pagini noi

#### 1 view

https://docs.djangoproject.com/en/4.1/topics/http/views/

https://docs.djangoproject.com/en/4.1/topics/class-based-views/

https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/

https://docs.djangoproject.com/en/4.1/ref/views/

https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/

Deschidem fisierul ```views.py``` din folderul ```numele_aplicatiei```

Creem o functie noua:

```python
def pagina_noua_view(
        request):  # orice function based view isi primeste request-ul prin parametru. Daca avem parametri in url, ii vom adauga dupa request.
    return render(request, "page.html",
                  {})  # functia render imperecheaza codul din template cu datele dinamice din dictionarul de context si returneaza raspuns de succes cu continutul html rezultat.
```

#### 1 template

In folderul principal creem subfolderul templates.

Ne asiguram ca folderul ```templates``` e adaugat in constanta ```TEMPLATES``` din ```settings.py```

```python
TEMPLATES = {
    # ...
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    # ...
}
```

####                                                   

Creem fisierul page.html, in care adaugam continutul.

```html

<html lang="en">
<head>
    <title>titlul paginii</title>
</head>
<body>
continutul paginii
</body>
</html>
```

#### 1 url

Deschidem fisierul urls.py din folderul numele_aplicatiei.

Adaugam un nou path un lista urlpatterns:

```python
# products/urls.py
urlpatterns = [  # lista obligatorie pentru a integra in urls.py al proiectului
    path('page/', views.page, name="page"),  # url-ul individual spre o pagina
]
```

Apoi deschidem browserul si navigam spre [http://127.0.0.1/page](http://127.0.0.1/page)

### Mostenirea template-urilor

Avand in vedere un template ```base.html```, putem pune un inlocuitor pentru viitorul cod din mostenitori:

```html

<html lang="en">
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
{% block body %}{% endblock %}
</body>
</html>
```

###                                                     

Putem mosteni template-ul si putem defini continutul individual, pastrand scheletul din ```base.html```.

```html
{% extends 'base.html' %}

{% block title %}Titlu propriu al paginii{% endblock %}
{% block body %}
<div>
    Continut propriu al paginii
</div>
{% endblock %}
```

### Trimiterea datelor dinamice spre template-uri

Orice fel de date dinamice avem de trimis, trebuiesc adaugate in dictionarul de context.

```python
def page_view(request):
    products = Product.objects.all()
    return render(request, 'page.html', {'products': products})
```

Apoi, in template-ul ```page.html``` putem folosi variabila ```{{ products }}```.

```html
{% extends 'base.html' %}

{% block body %}
{{ products }}
{% for product in products %}
{{ product }}
{% endfor %}
{% endblock %}
```

### Formulare

Django are abilitatea sa genereze formulare HTML pe baza unor clase definite de noi, sau prin legarea la un anumit
model.

Definitia formularelor se face in ```forms.py```, si vom folosi valori din ```forms.```

Clasa ```ModelForm``` imi permite generarea unui formular pe baza modelului specificat.
Orice schimbare la structura bazei de date se va regasi in formularul HTML.

```python
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  # ori string-ul __all__, ori o lista de string-uri
        widgets = {}
```

###                                                

Daca dorim sa facem override la controalele HTML generate, avem proprietatea optionala ```widgets = ```, unde punem un
dictionar cu:

- chei: nume de coloane puse intre ghilimele
- valori: instante din clase oferite de pachetul forms

Orice instanta de control HTML suporta proprietatea ```attrs```, populata cu un dictionar de:

- chei: atribute HTML
- valori: valori atribute HTML

```python
widgets = {
    'name': forms.TextInput(attrs={'required': True}),
    'price': forms.NumberInput(attrs={'required': True}),
}
```

### Class based Views:

Cand avem de a face cu create/update/delete/list/details al unui singur obiect, putem folosi view-uri bazate pe clase

#### TemplateView

Pentru un view care stie doar sa incarce un template ca raspuns, putem folosi ```TemplateView```

```python
class HomePageView(TemplateView):
    template_name = 'nume_template.html'
```

#### DetailView

DetailView stie sa scoata din baza de date 1 obiect dupa primary key, si sa il trimita spre template-ul specificat.

```python
class ProductDetailView(DetailView):
    model = Product  # modelul de care se ocupa
    template_name = 'product_detail.html'  # template-ul pe care il incarca
    context_object_name = 'product'  # numele de variabila din dinctionarul de context / django template language
```

#### ListView

ListView stie sa citeasca o lista de obiecte dupa proprietatea ```queryset``` sau metoda ```get_queryset()```, si o
trimia spre template-ul specificat in proprietatea ```tmeplate_name``` cu numele de variabila setat
pe ```context_obect_name```.

```python
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.all()
```

#### CreateView

CreateView stie sa incarce un formular HTML intr-un template, si sa creeze un obiect pe baza datelor completate.

In caz de succes, redirecteaza spre url-ul specificat. In caz de eroare, va fi afisata eroarea in pagina.

```python
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('product_list')
```

#### UpdateView

Echivalent cu CreateView, dar se ocupa de opdate pe obiectul respectiv.

```python
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')
```

#### DeleteView

Afiseaza un mesaj de confirmare, dupa care sterge un obiect din baza de date si redirecteaza spre ```success_url```.

```python
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
```

### URL-uri aplicatie

In fisierul ```urls.py``` al aplicatiei, intruducem cate un path nou pentru paginile noastre

Orice aplicatie ofera o lista de URL-uri accesibile pentru a oferi functionalitate.

Folosim functia ```path()``` cu cei 3 parametri:

- sufixul din URL
- legatura cu un view:
    - referinta spre o functie
    - apel pe metoda ```as_view()``` pe o clasa
- un nume unic cu ajutorul caruia putem genera URL-ul complet

```python
urlpatterns = [
    path('', views.homepage_view, name="homepage"),  # referinta spre functie
    path('create_product/', views.ProductCreateView.as_view(), name="product_create"),
    # apel pe as_view() pentru clasa 
]
```

## Test driven development

Test driven development e o procedura de dezvoltare a unui proiect (scriere a codului), in care se impune scrierea
testelor inaintea implementarii functionalitatii.

1. Writes first tests, and basic skeleton of non-working code.
2. Run tests, tests fail
3. Develop the feature
4. Run tests, tests pass
5. Client asks for a change, or feature, go to 1.

### Avantaje

- cod mult mai bine documentat
- schimbarile cerute de client sunt implementate mult mai repede in cod
- testele sunt verificate de developeri cand implementeaza functionalitatea

### Dezavantaje

- necesita aproape dublul orelor sau oamenilor
- necesita ca toata echipa sa fie pe TDD

## Behaivour driven development

Behaivour driven development este o procedura de dezvoltare a unui proiect provenita din Test Driven Development.

Folosind acelasi ciclu de dezvoltare, BDD ne adauga si limbajul:

- Given: datele problemei
- When: apelare functionalitate din aplicatie
- Then: assert pentru asigurarea validitatii datelor

## Principiile FIRST

- Fast
- Isolated/Independent
- Repeatable
- Self-validating
- Thorough

## Agile - metodologii pentru cod

- CI/CD = Continuous integration, coninuous delivery
- Pair programming = 2 programatori care lucreaza pe acelasi cod, pe acelasi calculator sau prin share screen.

## SCRUM - niste sedinte si roluri pe proiect

### Roluri

- Lead developer
- developers
- Scrum master
- Product owner

### Sedinte

- Estimation
- Mid review
- Retrospective
- Daily standup

### Other terms

- Product increment = o noua etapa a proiectului (set de feature-uri, redesign, etc)
- Sprint = cea mai mica unitate de masura in dezvoltarea unui proiect
- Backlog = lista de task-uri ce urmeaza a fi facute pe Product Increment

## Utils

