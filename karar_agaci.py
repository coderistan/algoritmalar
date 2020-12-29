# coding: utf-8
# Eldeki verilerden, bir karar ağacı oluşturarak
# mevcut şartlarda oyun olup olmayacağına karar veren algoritma

import math
import pandas

def entropi(t:pandas.DataFrame,d:str):
    """t: tablo , d: değer"""
    s = t[d].count() # sütun veri sayısı
    c = t[d].value_counts() # sütundaki verilerin frekansı
    h = sum((i/s)*math.log(i/s,2) for i in c) * (-1) # entropi
    return h

def kazanc(t:pandas.DataFrame,d:str):
    """t: tablo , d: değer"""
    c = t[d].value_counts() # C değerleri yani sınıf çeşitleri de diyebiliriz
    result = {}

    for i in c.keys():
        l = t[t[d] == i][hedef].value_counts() # karşılaştırılan sütunun, hedef sütundaki değerlerinin karşılığı ve frekansı
        h = sum((l[k]/int(c[i]))*math.log(l[k]/int(c[i]),2) for k in l.keys()) * (-1)
        result[i] = h
    
    l = t[d].count()
    h = sum((c[i]/l)*k for i,k in result.items())
    sonuc = hedef_entropi - h
    n = entropi(t,d)

    return sonuc/n # daha iyi sonuç veren bilgi bölünmesi kullanıldı

# karar ağacı hangi nitelikten dallanmalı?
def find_root(t:pandas.DataFrame):
    _root = None
    enb = 0

    # daha sonra tüm nitelikler için tek tek kazanç hesaplaması yapılır
    for i in t:
        if i==hedef:
            continue

        temp = kazanc(t,i)
        if temp > enb:
            enb = temp
            _root = i
    return _root

def get_sub_tree(t:pandas.DataFrame,d:str,result:dict):

    degerler = t[d].value_counts()
    result[d] = {}

    for i in degerler.keys():
        if i==d:
            continue

        alt_agac = t[t[d]==i]
        # Her bir dalına bir alt ağaç veya düğüm bağlanır
        # eğer alt ağaca gerek yoksa düğüm
        # alt ağaca gerek varsa recursive çağrı
        temp = alt_agac[hedef].value_counts()
        if temp.count() == 1:
            result[d][i] = temp.keys()[0]
            
        else:
            x = alt_agac.drop(d,axis=1)

            temp = find_root(x)
            result[d][i] = temp
            get_sub_tree(x,temp,result)
            
    return result

tablo = pandas.read_csv("files/oyun.csv")
print("Dosya okundu")
hedef = "oyun"

hedef_entropi = entropi(tablo,hedef)
root = find_root(tablo)

print("Birinci dallanma: ",root)
result = get_sub_tree(tablo,root,{})

print("\nKarar ağacı sonu")
for i,k in result.items():
    print(i,k)