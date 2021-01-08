# coding: utf-8
import math
import itertools

# iki gözlem arasında kolay ve soyut bir karşılaştırma yapma
# ve iki gözlem değerini kolay bir şekilde birleştirme amacı taşır
class Gozlem:
    def __init__(self,index,degerler):
        self.index_list = [index]
        self.degerler = degerler
    
    def mesafe(self,other):
        if len(self.index_list) > 1 or len(other.index_list) > 1:
            result = math.inf

            for i,k in itertools.product(self.index_list,other.index_list):
                
                temp = uzakliklar[i][k]
                
                if temp <= result:
                    result = temp
            
            return result

        else:
            if uzakliklar[self.index_list[0]][other.index_list[0]] == -1:
                result = sum((i[0]-i[1])**2 for i in zip(self.degerler,other.degerler)) ** 0.5
            else:
                result = uzakliklar[self.index_list[0]][other.index_list[0]]

            return result

    def birlesim(self,other):
        self.index_list.extend(other.index_list)
        self.index_list = sorted(self.index_list)

    def __str__(self):
        return "[" + ",".join(str(i) for i in self.index_list) + "]"

# gözlem verilerini işlenebilir hale getirme
gozlem_veriler = [
    [5.1,3.5,1.4,.2],  # -> setosa
    [6.4,3.1,5.5,1.8], # -> virginica
    [6.3,3.4,5.6,2.4], # -> virginica
    [6.4,2.7,5.3,1.9], # -> virginica
    [4.9,3,1.4,.2],    # -> setosa
    [5.4,3.9,1.7,.4],  # -> setosa
    [5.6,2.8,4.9,2],   # -> virginica
]

veriler = []
for index,i in enumerate(gozlem_veriler):
    veriler.append(Gozlem(index,i))
# ------------------------------------------^

# uzakliklar matrisi -------------------------
N = len(veriler)
uzakliklar= []
for i in range(N):
    uzakliklar.append([-1 for k in range(N)])
# -------------------------------------------^

alt_kume = [0,0]
kumeler = []
resume = True

while resume:
    resume = False
    N = len(veriler)
    enk = math.inf # en küçük
    
    for index in range(N):
        pivot = veriler[index] # sıradaki gözlem

        if len(veriler[index].index_list) == 1:
            resume = True

        for i in range(index+1,N):
            result = pivot.mesafe(veriler[i])

            if result <= enk:
                enk = result
                alt_kume = [index,i]
            
            if uzakliklar[i][index] == -1:
                uzakliklar[i][index] = result
                uzakliklar[index][i] = result

    if len(veriler) > 1:
        veriler[alt_kume[0]].birlesim(veriler[alt_kume[1]])
        del veriler[alt_kume[1]]
    else:
        resume = False

    kumeler.append([str(i) for i in veriler])

for index,i in enumerate(kumeler):
    print("Aşama",index+1)
    for k in i:
        print(k)

    print("-"*20)