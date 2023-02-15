# media ponderata

# a, b, c = 7, 5, 9
# p, q, r = 3, 2, 7
# print((a*p+b*q+c*r)/(p+q+r))

def media_ponderata():
    valoare = (7, 5, 9)
    pondere = (3, 2, 7)
    sumprod_valpond = (valoare[0] * pondere[0]) + (valoare[1] * pondere[1]) + (valoare[2] * pondere[2])
    sum_pond = sum(pondere)
    mp = sumprod_valpond / sum_pond
    return mp
