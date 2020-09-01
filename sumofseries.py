
def series_sum(n):
	sum=0
	if n==1:
		return "%.2f"%1
	elif n==0:
		return "%.2f"%0
	else:
		for i in range(4,3*n,3):
			sum+=1/(i)
		return "%.2f"%(sum+1)

k=series_sum()
print(k)