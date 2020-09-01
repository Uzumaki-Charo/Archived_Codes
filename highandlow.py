def highandlow(numbers):
	numbers=numbers.split()
	#print(numbers)
	numbers=list(map(int,numbers))
	#print(numbers)
# m=-1
# for i in range(0,len(numbers)):
# 	if numbers[i]>m:
# 		m=numbers[i]
	numbers=[max(numbers),min(numbers)]
	return "%i %i"%(numbers[0],numbers[1])


numbers="1 2 4 -5 234 123 -10"
g=highandlow(numbers)
print(type(g))
