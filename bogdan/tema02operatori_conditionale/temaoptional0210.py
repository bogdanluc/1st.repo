# 10. Avand stringul '0123456789'
# ● Aﬁșați doar numerele pare
# ● Aﬁșați doar numerele impare
# (hint: folositi slicing, controlați din pas)

string123 = '0123456789'
size = len(string123)

print(string123[:size:2]) # afiseaza numerele pare din acest string => 0,2,4,6,8
print(string123[1], string123[3], string123[5], string123[7], string123[9])

for i in range(1, size, 2):
    print(i)
for i in range(0, size, 2):
    print(i)