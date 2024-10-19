# coding: utf-8
# http://mathforum.org/advanced/robertd/manhattan.html

import math

def solution(dimension):
    return math.factorial(dimension+dimension) / (math.factorial(dimension)*math.factorial(dimension))

print(solution(20))