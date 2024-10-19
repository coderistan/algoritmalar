# coding: utf-8
import math
import itertools

# iki gözlem arasında kolay ve soyut bir karşılaştırma yapma
# ve iki gözlem değerini kolay bir şekilde birleştirme amacı taşır
class Gozlem:
    def __init__(self,root,index,values):
        self.root = root
        self.index_list = [index]
        self.values = values
    
    def distance_from(self,other):
        if len(self.index_list) > 1 or len(other.index_list) > 1:
            result = math.inf

            for i,k in itertools.product(self.index_list,other.index_list):
                
                temp = self.root.distances[i][k]
                
                if temp <= result:
                    result = temp
            
            return result

        else:
            if self.root.distances[self.index_list[0]][other.index_list[0]] == -1:
                result = sum((i[0]-i[1])**2 for i in zip(self.values,other.values)) ** 0.5
                self.root.distances[self.index_list[0]][other.index_list[0]] = result
                self.root.distances[other.index_list[0]][self.index_list[0]] = result
            else:
                result = self.root.distances[self.index_list[0]][other.index_list[0]]

            return result

    def union(self,other):
        self.index_list.extend(other.index_list)
        self.index_list = sorted(self.index_list)

    def __str__(self):
        return "[" + ",".join(str(i) for i in self.index_list) + "]"

class kNNClassification:
    def __init__(self,data):
        self.data = data

        self.N = len(data)
        self.prepare_data()

        self.initialization()
        

    def prepare_data(self):
        self.values = []

        for index,i in enumerate(self.data):
            self.values.append(Gozlem(self,index,i))

    def initialization(self):
        self.sets = []
        self.distances = []

        for i in range(self.N):
            self.distances.append([-1 for k in range(self.N)])

    def start(self):
        subset = [0,0]
        resume = True

        while resume:
            resume = False
            mnm = math.inf # en küçük
            self.N = len(self.values)

            for index in range(self.N):
                pivot = self.values[index] # sıradaki gözlem

                if len(self.values[index].index_list) == 1:
                    resume = True

                for i in range(index+1,self.N):
                    result = pivot.distance_from(self.values[i])

                    if result <= mnm:
                        mnm = result
                        subset = [index,i]

            if len(self.values) > 1:
                self.values[subset[0]].union(self.values[subset[1]])
                del self.values[subset[1]]
            else:
                resume = False

            self.sets.append([str(i) for i in self.values])

            print("STAGE ({})".format(len(self.data)-index))
            print("-"*20)
            
            for i in self.values:
                print(i)
            


gozlem_veriler = [
    [6.4,3.1,5.5,1.8], # -> virginica
    [6.3,3.4,5.6,2.4], # -> virginica
    [6.4,2.7,5.3,1.9], # -> virginica
    [4.9,3,1.4,.2],    # -> setosa
    [5.4,3.9,1.7,.4],  # -> setosa
    [5.6,2.8,4.9,2],   # -> virginica
    [5.1,3.5,1.4,.2],  # -> setosa
]

knn = kNNClassification(gozlem_veriler)
knn.start()
