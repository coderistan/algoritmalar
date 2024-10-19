# coding: utf-8

"""
Kurulan modelin açıklayıcılığı R^2 ile bulunur. Yani 1 - rss/tss. 0 ve 1 arasında değer alır. 
Eğer 1'e yakınsa, bu durum bağımsız değişkenlerin, bağımlı değişkenleri iyi açıkladığını gösterir
"""

import pandas

denklem = lambda b0,b1,x:b0 + b1*x # modelin kurulması

def b1_calculate():
    pay = 0
    for i in range(x.size):
        pay += (x[i] - x_)*(y[i] - y_)
    
    payda = 0
    for i in range(x.size):
        payda += (x[i] - x_)**2

    return pay/payda

def rss():
    toplam = 0
    for i in range(x.size):
        fark = y[i] - denklem(b0,b1,x[i])
        toplam = toplam + fark**2

    return toplam

def tss():
    toplam = 0
    for i in range(y.size):
        fark = y[i] - y_
        toplam = toplam + fark**2
    return toplam

def ess():
    toplam = 0
    for i in range(y.size):
        fark = denklem(b0,b1,x[i]) - y_
        toplam = toplam + fark**2
    return toplam

veri = pandas.read_csv("files/Advertising.csv")

x = veri["TV"]
y = veri["Sales"]

x_ = x.mean()
y_ = y.mean()
b1 = b1_calculate()
b0 = y_ - b1*x_

print("y = {:.2}".format(b0),"+ {:.2}".format(b1),"* x")
print("Aralarındaki ilişki katsayısı: ",(1-rss()/tss()))