# coding: utf-8
# @coderistan
# çift fibonacci sayılarının toplamı(max 4 milyon)

x,y = 1,1
toplam=0

while(toplam<4000000):
    x,y=y,x+y
    if(y%2==0):
        toplam+=y
        
print(toplam)
