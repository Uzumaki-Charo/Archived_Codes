import time

def generatefactnum(num):
	if num==0:
		return 1
	else:
		return num*generatefactnum(num-1)
def sumdigit(results):
	n=0
	result=generatefactnum(results)
	while result//10!=0:
		n=n+result%10
		result=result//10
	return n+result
start=time.time()
results=sumdigit(100)
elapsed=time.time()-start
print("The sum is %s found in %s seconds"%(results,elapsed))