#coding: utf-8

def solution(N):
    return (sum([i for i in range(N+1)])**2) - sum([i**2 for i in range(N+1)])

print(solution(100))