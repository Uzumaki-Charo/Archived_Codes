# import time
# import math
# array=[]
# isum=[]


# def checkifabund(num):
# 	sum=0
# 	for i in range(1,(num//2)+1):
# 		if num%i==0:
# 			sum+=i
# 	if num<sum:
# 		#print("checkifabund",num,sum)
# 		array.append(num)



# # def arrayab(num):
# # 	array.append(num)
# 	#print(array)
# 	# for i in range(0,len(array)):
# 	# 	if i==0 and 2*array[len(array)-1]<28124:
# 	# 		nsum+=2*array[len(array)-1]
# 	# 		#print("2i",nsum)
# 	# 	if i<len(array)-1 and len(array)>1 and (array[0]+array[len(array)-1])<28124:
# 	# 		nsum=nsum+(array[i]+array[len(array)-1])
# 	# 		#print("i+end",array[i]+array[len(array)-1])
# 	# 	# if nsum>28124:
# 	# 	# 	nsum=nsum-2*array[len(array)-1]
# 	# #print("nsum",nsum)
# 	# if 2*array[len(array)-1]<28124 and (array[0]+array[len(array)-1])<28124:
# 	# 	msum.append(nsum)
# 	# return msum


# def generate():


# 	for i in range(1,28124):
# 		isum.append(i)
# 		checkifabund(i)

# # start=time.time()
# # result=generate()
# # elapsed=time.time()-start

# #print("The result is %s found in %s"%(result,elapsed))
# # print(checkifabund(12),arrayab(12))


# generate()
# for i in range(0,len(array)):
# 	for j in range(i,28123):
# 		if array[i]+array[j]<28123:
# 			isum[array[i]+array[j]]=0
# 		else: break
# #print (isum)
# print (sum(isum))

#http://radiusofcircle.blogspot.com

#time module for calculating execution time
import time

#square root from math module
from math import sqrt

#time at the start of execution
start = time.time()

#Function used from problem 21
def divisors(n):
	"""This function will generate 
	divisors of given number
	Example: divisors(28) will give
	[1,2,4,7,14]"""
	divs = [1]
	for i in range(2,int(sqrt(n))+1):
		if n%i == 0:
			divs.extend([i,n/i])
	return list(set(divs))

#list to store the values of abundant numbers
ab = []

#For loop to generate the abundant numbers
for i in range(12,28123):
	if sum(divisors(i))>i:
		ab.append(i)

#first let us assume all the numbers are 
#not sum of abundant numbers
non_ab_sum = [x for x in range(28123)]

#for loop to generate sum of two 
#abundant numbers
for i in range(len(ab)):
	for j in range(i,28123):
		if ab[i]+ab[j] < 28123:
			#negating the value of the abundant sum
			non_ab_sum[ab[i]+ab[j]] = 0
		else:
			break

#printing the value of the sum of non abundant sum
print (sum(non_ab_sum))
        
#printing the total execution time
print (time.time() -start)