# 6. Având dict:
# pret_masini = {'Dacia': 6800,'Lăstun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.

pret_masini = {'Dacia': 6800, 'Lăstun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000}

marca = pret_masini.keys()
pret = pret_masini.values()

for pret in pret_masini.values():
    if pret <= 15000:
        print(pret)
