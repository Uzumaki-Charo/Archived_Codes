import time

def generatedivisor(n):
	s=[]
	for i in range(1, (n//2)+1):
		if n%i==0:
			s.append(i)
	return s

def sumdivisor(d):
	f=0
	for i in range(0,len(d)):
		f=f+d[i]
	return f

def checkifequal(n):
	div1=generatedivisor(n)
	b1=sumdivisor(div1)
	div2=generatedivisor(b1)
	b2=sumdivisor(div2)
	i=0
	if n==b2 and n!=b1:
		return n
	else:
		return 0
def run(i):
	i=0
	for j in range(3,10000):
		k=checkifequal(j)
		i=i+k
	return i

start=time.time()
# result1=generatedivisor(220)
# result2=sumdivisor(result1)
# result3=checkifequal(220)
result=run(1)
elapsed=time.time()-start

# print(result1,result2)
print("result is %s found in %s"%(result,elapsed))
