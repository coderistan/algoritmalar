# 10001. asal sayıyı bulma

def is_prime(num):
    if num > 1:
        for i in range(2,int(num/2)):
            if (num % i) == 0:
                return False
        else:
            return True

sayac = 0
sayi = 0

while(sayac<=10001):
    sayi+=1
    if(is_prime(sayi)):
        sayac+=1
    
print(sayi)