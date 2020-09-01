#array=[];
#arraya=[];
sum=0;

for i in range(1,1000):
	#array[i-1]=i;
	remainer3=i%3;
	remainer5=i%5;
	if (remainer3==0) or (remainer5==0):
		sum=sum+i;
		

print("sum=",sum)