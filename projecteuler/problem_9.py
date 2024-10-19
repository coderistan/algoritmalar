import itertools

for i in itertools.combinations(range(500),3):
    a,b,c = i[0],i[1],i[2]
    if a**2 + b**2 == c**2 and (a+b+c) == 1000:
	print(a*b*c)
	break
