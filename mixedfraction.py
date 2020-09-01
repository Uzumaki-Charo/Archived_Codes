import math
def mixed_fraction(s):
	num = s.split('/')
	x = int(num[0])
	y = int(num[1])

	if x//y <0:
		minus = True
	else: 
		minus = False

	x = abs(x)
	y = abs(y)

	if y == 0:
		return None
	elif x == 0:
		return '0'
	else:
		if x<y:
			for i in range(int(math.sqrt(x))+2,1,-1):
				if (x%i==0) and (y%i==0):
					x = x//i
					y = y//i
			return f'{x}/{y}' if minus == False else f'-{x}/{y}'
		else:
			a = x//y
			remainder = x%y

			for i in range(int(math.sqrt(remainder))+2,1,-1):
				if (remainder%i==0) and (y%i==0):
					remainder = remainder//i
					y = y//i

			if a == 0:
				return f'{remainder}/{y}' if minus ==False else f'-{remainder}/{y}'
			elif remainder == 0:
				return f'{a}' if minus ==False else f'-{a}'
			else:
				return f'{a} {remainder}/{y}' if minus ==False else f'-{a} {remainder}/{y}'


def findppcm(a,b):
	a_list = []

	if a%2==0:
		a_list = [2]

	else:
		for i in range(3,int(math.sqrt(a)+1), 2):
			if a%i==0 and b%i == 0:
				a_list.append(i)

	return a_list	


from fractions import Fraction

def mixed_fraction(s):
    f = Fraction(*map(int, s.split('/')))
    if f.denominator == 1: return str(f.numerator)
    n = abs(f.numerator) / f.denominator * (1 if f.numerator > 0 else -1)
    f = abs(f - n) if n else f - n
    return "{} {}".format(n, f) if n else str(f)

from fractions import gcd

def mixed_fraction(s):
    x, y = map(int, s.split('/'))
    signx = x/abs(x) if x else 1
    signy = y/abs(y) if y else 1
    sign = signx * signy
    x, y = map(abs, (x, y))
    a, b = divmod(x, y)
    g = gcd(b, y)
    b, c = b/g, y/g
    result = (str(a) * bool(a) +
               ' ' * bool(a) * bool(b) +
               (str(b) + '/' + str(c)) * bool(b))
    if not result:
        return '0'
    if sign < 0:
        result = '-' + result
    return result
		

#print(mixed_fraction('-4704076/8879344'))
#print(mixed_fraction('42/9'))
print(mixed_fraction('4/6'))
#print(mixed_fraction('0/18891'))
print(mixed_fraction('6/3'))
#print(findppcm(740943,7310199))