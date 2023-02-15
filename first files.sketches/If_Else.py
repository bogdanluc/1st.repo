#Flow control - if else
       # evalueaza conditii si bifurca codul in functie de rezultate

print('pornim radio')
piesa_faina = True

if piesa_faina == False:
       print('dam mai tare')
       print('fedonam')
print('oprim radio')


# if - else
# daca numarul este par printam acest lucru altfel printam impar

numar = 3
# ce inseamna par? se imparte exact la 2 si impartirea da rest 0

if numar % 2 == 0:
       print('numar par')
else:
       print('impar')

# este un numar pozitiv?

nr = 0

if nr > 0:
       print("numar pozitiv")
else:
       print('nu este pozitiv')

# if, else if, else
# cum ne saluta robotelul in functie de ora

# luam date de la tastatura, ne asiguram ca sunt transformate din string in int
# ora = int(input('Introdu ora'))
# if ora < 0:
#        print('ora negativa')
# elif ora <= 11:
#        print('buna dimineata')
# elif ora <= 12:
#        print('buna ziua')
# elif ora <= 23:
#        print('buna seara')
# else:
#        print('fuck off')
#
# viteza = int(input('what speed'))
# if viteza < 0:
#        print('viteza invalida')
# elif viteza == 0:
#        print('stationeaza')
# elif viteza <= 100:
#        print('viteza medie')
# elif viteza <= 200:
#        print('viteza mare')
# else:print('fuck off')

# comentare, decomentare CTRL + /

# robotelul telefonic

optiune = int(input('alege o optiune'))
if optiune == 0:
       print('meniu anterior')
elif optiune == 1:
       print('romana')
elif optiune == 2:
       print('engleza')
else:print('optiune invalida')