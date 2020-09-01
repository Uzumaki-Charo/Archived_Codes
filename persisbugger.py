import time 
count=[0]


def persist(num):
	array=[]
	count=[]
	i=1
	while num!=0:
		n=num%10
		num=num//10
		array.append(n)
	if len(array)==1:
		return 0
	for j in range(0,len(array)):
		i=i*array[j]
	if i//10!=0:
		count.append(1)
		return persist(i)
	else:
		return sum(count)+1

def persistence(num):
	if num//10==0:
		return sum(count)
	elif num//10!=0:
		#count.append(1)
		k=(num%10)*persistence(num//10)
		return k
def persistence(n):
    res = 0
    temp = 1
    while (n > 9):
        if temp == 1:
          temp = n % 10
        n -= n %10
        n /= 10
        temp *= (n % 10)
        if (n <= 9) :
          n = temp
          temp = 1
          res += 1
    return res

#k=persist(25)
k=persistence(999)
print(k)