# coding:utf-8
# @coderistan
# asal bölenlerin en büyüğünü bulmak
from math import sqrt

def next_prime(max_number):
    for i in range(3,max_number):
        if(i%2==0):
            continue
        else:
            find=True
            for k in range(3,int(sqrt(i))):
                if(i%k==0):
                    find=False
                    break
            if(find):
                yield i

def hesapla(sayi):
    asal = next_prime(max_number=10000)
    result = 0
    siradaki_asal=2
    
    while(sayi>1):
        if(sayi%siradaki_asal==0):
            result = siradaki_asal if(siradaki_asal!=result and siradaki_asal>result) else result
            sayi=sayi/siradaki_asal
        else:
            siradaki_asal=next(asal)
    return result

print(hesapla(600851475143))
    
