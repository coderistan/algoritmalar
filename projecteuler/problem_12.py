from functools import reduce
import math
import timeit

def get_prime_factors(number):
	result = []
	c = 0

	if(number == 0):
		return result

	while number%2 == 0:
		number = int(number/2)
		c += 1

	result.append((2,c))

	for i in range(3,int(math.sqrt(number))+1,2):
		c = 0

		while number%i == 0:
			number = number/i
			c+=1
		result.append((i,c))
		c = 0

	if(number>2):
		result.append((int(number),1))
	return result

def main():
	i = 0
	while True:
		sayi = int((i*(i+1)/2))
		liste = get_prime_factors(sayi)
		if(not liste):
			i += 1
			continue

		carpim = reduce(lambda a,b:a*b,[y+1 for x,y in liste])
		i += 1

		print(sayi,carpim)
		if(carpim >= 500):
			break
main()