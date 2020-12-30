# coding: utf-8
# Graf için en kısa yolu dinamik programlama ile bulma

import math

graf = [
    #0  1  2  3  4  5  6  7  8  9 10 11
    [0, 9, 7, 3, 2, 0, 0, 0, 0, 0, 0, 0],  # 0
    [0, 0, 0, 0, 0, 4, 2, 1, 0, 0, 0, 0],  # 1
    [0, 0, 0, 0, 0, 2, 7, 0, 0, 0, 0, 0],  # 2
    [0, 0, 0, 0, 0, 0, 0,11, 0, 0, 0, 0],  # 3
    [0, 0, 0, 0, 0, 0,11, 8, 0, 0, 0, 0],  # 4
    [0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 0, 0],  # 5
    [0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0],  # 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 0],  # 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],  # 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],  # 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],  # 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
]
 
n = 12       # düğüm sayısı
cost = [0]*n # maliyetler
d = [0]*n    # yön (direction)

cost[n-1] = 0  # son düğümün kendisine maliyeti sıfırdır
d[n-1] = 0     # son düğümün yönlendirmesi yok

for i in range(n-2,-1,-1):
    minimum = math.inf
    for k in range(i+1,n):
        if(graf[i][k] != 0 and (graf[i][k] + cost[k]) < minimum):
            minimum = graf[i][k] + cost[k]
            d[i] = k
        
        cost[i] = minimum
    

print("En kısa yol güzergâhı")
index = 0

while d[index] != 0: # son düğüme gelinince
    print(d[index]+1," -> ",end="")
    index = d[index]

print("SON")