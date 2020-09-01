import time

def check(num):
	if num//10**(999)!=0:
		return True
def generate():
	num=0
	i=2
	n0=1
	n1=1
	while True:
		num=n0+n1
		n0=n1
		n1=num
		i+=1
		if check(num):
			return i

start=time.time()
result=generate()
elapsed=time.time()-start

print("result is %s found in %s"%(result,elapsed))
