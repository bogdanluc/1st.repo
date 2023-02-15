# 9. Citește o literă de la tastatură.
# Veriﬁcă și aﬁșează dacă este vocală sau nu


lit = input('Is the letter a vowel? ')
a, e, i, o, u = 'a', 'e','i','o','u'
if lit == a or lit == e or lit == i or lit == o or lit == u:
    print(True)
else:
    print(False)


