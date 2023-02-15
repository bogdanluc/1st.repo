print(string[len(string) // 2])

st = input("Pune string: ")
cuvant1 = st.split(" ",1).__getitem__(0)
cuvant2 = st.split(" ",1).__getitem__(1)
print(cuvant1)
print(cuvant2)

print("Fiecare variabila: ",st.split(" ",1).__getitem__(0) ,"\n", st.split(" ",1).__getitem__(1))

print("modalitatea 2")
mod_string2 = coral[:-x]
print(mod_string2)

7. first_5 = (coral[:5])
last_5 = coral[-5:]
print(first_5 + last_5)

8
index_string_rock = (coral.find("rock"))
coral2 = coral[:index_string_rock]
print(coral2)

9
string = input("Introdu un string: ")
primul_ch = string[:1]
ultimul_ch = string[-1:]
if primul_ch == ultimul_ch:
    print("Primul si ultimul caracter este identic:", primul_ch, "=", ultimul_ch)
else:
    print("Primul si ultimul caracter NU este identic:", primul_ch, ultimul_ch)

    11 import random
    dice_roll = random.randint(1, 6)
    numar = int(input("Ghiceste un numar de la 1 la 6: "))
    print("Zarul este: ", dice_roll)
    if dice_roll == numar:
        print("Ai ghicit. Felicitari! Ai ales ", numar, "si zarul a fost", dice_roll)
    if dice_roll > numar:
        print("Ai pierdut. Ai ales un numar mai mic. Ai ales ", numar, "si zarul a fost", dice_roll)
    if dice_roll < numar:
        print("Ai pierdut. Ai ales un numar mai mare. Ai ales ", numar, "dar a fost ", dice_roll)

