# coding: utf-8
import timeit

even = lambda x:int(x/2)
odd = lambda x:int(3*x) + 1

# Hızlı çözüm, fakat daha çok yer kaplama
hesaplanmis = {}
def chain(number):
	count = 0
	temp = number

	while number > 1:
		if number in hesaplanmis:
			count += hesaplanmis[number]
			del hesaplanmis[number]
			hesaplanmis[temp] = count
			return count+1

		else:
			if number%2 == 0:
				number = even(number)
			else:
				number = odd(number)

			count += 1

	if not (temp in hesaplanmis):
		hesaplanmis[temp] = count

	return count+1

# Yavaş çözüm, fakat daha az yer kaplama
def chain2(number):
	count = 0
	while number > 1:
		if number%2 == 0:
			number = even(number)
		else:
			number = odd(number)
		count += 1

	return count+1

# Hız testi
def time_test():
	code1 = """
max_chain = 0
result = 0

for i in range(1,1000):
	chain_size = chain(i)
	if chain_size >= max_chain:
		max_chain = chain_size
		result = i
	"""

	code2 = """
max_chain = 0
result = 0

for i in range(1,1000):
	chain_size = chain2(i)
	if chain_size >= max_chain:
		max_chain = chain_size
		result = i
	"""

	print("fonksiyon 1: ",timeit.timeit(code1,number=100,globals=globals()))
	print("fonksiyon 2: ",timeit.timeit(code2,number=100,globals=globals()))


# Çözüm
max_chain = 0
result = 0
for i in range(1,1000000):
	chain_size = chain(i)
	if chain_size >= max_chain:
		max_chain = chain_size
		result = i
print(result)