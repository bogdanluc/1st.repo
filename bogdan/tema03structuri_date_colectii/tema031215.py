# 12. Set: zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Aﬁșeaza zile_sapt

zile_sapt = {'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
print(zile_sapt)
zile_sapt.update({'luni'})
print(zile_sapt)

# 13.Folosește un if și veriﬁcă dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.

if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor din săptămânii.")
else:
    print("Weekend nu este un subset al zilelor din săptămânii.")

#14. Aﬁșează diferențele dintre aceste 2 seturi.

print(zile_sapt.difference(weekend))

#15. Aﬁșază intersecția elementelor din aceste 2 seturi.

print(zile_sapt.intersection(weekend))