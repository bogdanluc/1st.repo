# Scrieti un algoritm care genereaza un dictionar cu numarul de aparitii
# al fiecarui caracter dintr-un string, ignorand litere mici/mari.
# Ex: pentru "python the basics", vom avea {'p':1, 'y':1, 't':2,'h':2, ...}

proposition = 'Everything is electric'
letter = proposition.count('E')
ind = proposition[0:len(proposition)]
print((ind, ind.count('e')))



