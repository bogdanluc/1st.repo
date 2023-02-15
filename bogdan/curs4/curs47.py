#Fiind dat algoritmul pentru desenat un brad (de la Irina),
# sa se transforme in functie cu parametri de intrare, si apeluri la print().

# for i in range(6)
#     for j in range(i+1)
#         print('#',end='')
#         print(i)

def half_tree(base):
    for i in range(base):
        for j in range(i + 1):
            print('#', end='')
        print(i)

half_tree(79)