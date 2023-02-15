# def  media_aritmetica(a, b,c):
#     return(a+b+c)/3
#
# ma = media_aritmetica(5,8,3)
# print(ma)

def media_artimetica(*args):
    return sum(args) / len(args)


print(media_artimetica(1, 2))
print(media_artimetica(1, 2, 3, 4, 5, 6))