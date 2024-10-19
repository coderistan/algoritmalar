# coding: utf-8
# @coderistan
# Max 1000'e kadar sayılardan 3 veya 5'in katlarının toplamı

def cozum1():
    return sum([i for i in range(3,1000) if i%3==0 or i%5==0])

def cozum2():
    toplam = 0
    for i in range(3,1000):
        if(i%3==0 or i%5==0):
            toplam+=i
    return toplam
            
print(cozum1())
print(cozum2())
