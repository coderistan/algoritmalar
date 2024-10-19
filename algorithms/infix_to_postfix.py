# coding: utf-8

ifade = "a+b*c-d*e"
stack = list()
operator = {
	"+":1,
	"-":1,
	"/":2,
	"*":2,
	"(":3,
	")":3,
}

sonuc = ""

for i in ifade:
	# bir operator değil ise
	if i not in operator:
		sonuc += i

	elif i == "(":
		stack.append(i)

	elif i == ")":
		while len(stack):
			temp = stack.pop()
			if temp == "(":
				break
			sonuc+=temp

	elif len(stack) and stack[-1] != "(" and operator.get(i) <= operator.get(stack[-1]):
		while len(stack):
			sonuc += stack.pop()
		stack.append(i)

	# bu durumlar dışında kalanları stack'e ekliyoruz
	else:
		stack.append(i)

# Son olarak tüm stack'i boşaltıyoruz
while len(stack):
	sonuc += stack.pop()

print(sonuc)