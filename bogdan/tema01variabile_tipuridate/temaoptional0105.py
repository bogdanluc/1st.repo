'''5.Exercițiu: - citește un user de la tastatură; - citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => *** parola abcd => ****
'''

user = input('user: ')
passw = input('pass: ')
x = len(passw)
print(f'Parola pentru user {user} este {passw} si are {x} caractere')