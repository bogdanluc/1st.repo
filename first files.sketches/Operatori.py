'''
Recap:
        Variabile
        tipuri de date: char, int, String, double/float, boolean

        operatorii sunt de mai multe feluri:
        aritmetici - +, -, *, /, % (modulo - aflarea restului impartirii)
        de comparare: < >, ==, !=, <=, >= (!= - diferit)
        logici: and, or, ! (! - not)

        Flow control - if else
'''

a = 3
b = 5

print(a + b) # 3+5 = 8
print(a == b) # 3=5? => false
print(a > b or b > a) # => true
print(a == b or (b>3 and 6>a)) # true

# cu mama sau tata sau (cu bunica si bunicul)

mama = False
tata = False
bunicu = True
bunica = True
print(mama and tata or (bunicu or bunica)) #=> true