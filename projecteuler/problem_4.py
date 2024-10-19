#coding:utf-8
#@coderistan
# 3 basamaklı 2 sayının çarpımından max olan palindrom sayıyı bulma

def isPalindrome(number):
   return str(number)==str(number)[::-1]

def cozum1():
    big = max_i = max_k = 0
    for i in range(100,999):
        for k in range(100,999):
            if(isPalindrome(i*k)):
                (big,max_i,max_k) = (i*k,i,k) if i*k > big else (big,max_i,max_k)
    return big,max_i,max_k

def cozum2():
    # https://projecteuler.net/thread=4;post=1211
    big = max_i = max_k = 0
    for i in range(999,100,-1):
        for k in range(990,100,-11):
            if(isPalindrome(i*k)):
                (big,max_i,max_k) = (i*k,i,k) if i*k > big else (big,max_i,max_k)
    return big,max_i,max_k
