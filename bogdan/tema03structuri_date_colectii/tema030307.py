# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.

list_a = [3, 1, 0, 2]
list_b = [6, 5, 4]

list_c = list_a + list_b
print(list_c)

list_c = list_a.__add__(list_b)
print(list_c)

# 4. ● Sortează și aﬁșază lista generată la exercițiul anterior.
# ● Sortează numărul 0 folosind o funcție.
# ● Aﬁșaza iar lista.

list_c.sort(reverse=False)
print(list_c)
list_c.sort(reverse=True)
print(list_c)
print(min(list_c))

# 5. Folosind un if veriﬁcă lista generată la exercițiul 3 și aﬁșază:
# ● Lista este goală.
# ● Lista nu este goală.

if list_c == []:
    print('lista este goala')
else:
    print('lista nu este goala')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.

list_c.clear()

# 7. Copy paste la exercițiul 5. Veriﬁcă încă o dată.

if list_c == []:
    print('lista este goala')
else:
    print('lista nu este goala')
