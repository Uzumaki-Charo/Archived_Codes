def find_nb(m):
    # your code
    i=0
    n=1    
    while m>0:
    	i=n**3
    	n+=1
    	m=m-i
    	print(i,m,n)
    if m==0:
    	return n-1
    else: 
    	return -1



g=find_nb(1071225)
print(g)