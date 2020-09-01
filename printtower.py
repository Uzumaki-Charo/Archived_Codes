def tower(n):
	a=[""]*n
	for j in range(0,n):
		for i in range(0,2*n-1):
			if n-1-j<=i<n+j:
				a[j]+="".join("*")
			else:
				a[j]+="".join(" ")
	return a

	return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
	# return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]
	# length = n * 2 - 1
 #   	return ['{:^{}}'.format('*' * a, length) for a in xrange(1, length + 1, 2)]


k=tower(3)
print(k)

