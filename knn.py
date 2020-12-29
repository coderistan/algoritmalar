# coding: utf-8
import pandas as pd
from typing import List

def minimize(veriler:pd.DataFrame,sutunlar:List[int]=None):
    """
    Gelen verilerin bütün sütunlarını, veya sutunlar argümanı verildiyse
    ilgili sütunlarını minimize eden fonksiyon
    """
    if sutunlar:
        for sutun in sutunlar:
            if veriler.iloc[:,sutun].dtype.name == "object":
                # yalnızca sayısal veri içeren sütunlar
                continue
            
            max_deger = veriler.iloc[:,sutun].max()
            min_deger = veriler.iloc[:,sutun].min()

            veriler.iloc[:,sutun] = veriler.iloc[:,sutun].apply(
                    lambda x:(x-min_deger)/(max_deger-min_deger)
                )

    else:
        for nitelik in veriler:
            if veriler[nitelik].dtype.name == "object":
                # yalnızca sayısal veri içeren sütunlar
                continue

            max_deger = veriler[nitelik].max()
            min_deger = veriler[nitelik].min()

            veriler[nitelik] = veriler[nitelik].apply(
                lambda x:(x-min_deger)/(max_deger-min_deger)
                )

def minimize_gozlem(veriler:pd.DataFrame,gozlem:List[int]):
    """
    Gozlem verilerini minimize etme
    """
    for index,i in enumerate(gozlem):
        max_deger = veriler.iloc[:,index].max()
        min_deger = veriler.iloc[:,index].min()

        gozlem[index] = (i-min_deger) / (max_deger-min_deger)
    
    return gozlem

def distances(veriler:pd.DataFrame,gozlem:List[int],hedef:str):
    """
    Bir DataFrame içerisinde yer alan tüm satırların, gozlem
    verilerine olan uzaklığının hesaplanması. Hesaplanan uzaklıklar
    veriler DataFrame'ine distances sütunu olarak eklenir
    """
    sonuclar = []
    for satir in veriler.drop(hedef,axis=1).values:
        sonuclar.append(
            sum(
                (i[0]-i[1])**2 for i in zip(gozlem,satir)
            )
        )
    
    veriler["distances"] = sonuclar

veriler = pd.read_csv("files/iris.csv") # iris çiçeği verileri
tahmin = [5.6,2.5,3.9,2.1] # virginica -> %100
gozlem = minimize_gozlem(veriler,tahmin)

k = 4 # komşu sayısı
hedef = "variety"

# tabloyu minimize etme
minimize(veriler)

# tüm satırların uzaklığını hesaplama
distances(veriler,gozlem,hedef)

# uzaklıkları bulduktan sonra k komşuyu içeren verileri alıyoruz
sonuclar = veriler.iloc[veriler.distances.sort_values()[:k].keys()]
toplam = sonuclar[hedef].count()
# sonuclardaki sınıfların frekansı
sonuclar = sonuclar[hedef].value_counts()

for i in sonuclar.keys():
    print(i,"->","%",(sonuclar[i]/toplam)*100)