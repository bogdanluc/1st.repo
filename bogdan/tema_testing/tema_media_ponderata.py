# media ponderata

# a, b, c = 7, 5, 9
# p, q, r = 3, 2, 7
# print((a*p+b*q+c*r)/(p+q+r))

def media_ponderata(valoare, pondere):
    pondere_valoare = (valoare[0] * pondere[0]) + (valoare[1] * pondere[1]) + (valoare[2] * pondere[2])
    sum_pond = sum(pondere)
    mp = pondere_valoare / sum_pond
    return mp


valoare = (7, 5, 9)
pondere = (3, 2, 7)

print(media_ponderata(valoare, pondere))
