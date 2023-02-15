# variabila = date pe care le inregistram in memorie
    # pot fii de mai multe tipuri:
        #String - sir de caractere delimitate cu ' ' sau " "
        #int - numere intregi
        #float/double - numere zeciamle
        #boolean - True sau False
# #2
# nume = 'Calsberg'
# pret = 4
# procent_alcool = 4.9
# filtrata = True
# #3
# print(type(nume))
# print(type(pret))
# print(type(procent_alcool))
# print(type(filtrata))
# #4
# procent_alcool = round(procent_alcool)
# print(procent_alcool)
# print(type(procent_alcool))
# #5
# print(f'Berea {nume} are o alcoolemie de {procent_alcool} la suta')
# print(f'Se poate achizitiona la pretul de {pret} lei')
# print(filtrata == True)
# print(f'Pretul unui sixpack este de:')
# print(pret * 6)
# #6
# nume = input('Numele meu este ')
# prenume = input('Prenumele meu este: ')
# print(len(nume + prenume))
# #7
# lungimea = input('L:')
# latimea = input('l:')
# lungimea = int(lungimea)
# latimea = int(latimea)
# x = lungimea * latimea
# print(x)
# #8
propozitie = 'Coral is either the stupidest animal or the smartest rock'
# print(propozitie.count(' the '))
# #9
# print(propozitie.count('the'))
#10
assert propozitie == 'Coral is either the stupidest animal or the smartest rock'
########################################################################################
#1
nume = input('word:')
print(nume.isnumeric())





