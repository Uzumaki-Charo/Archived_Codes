def diamond(n):
	if n>0 and n%2!=0:
		a=[0]*n
		l=0
		for k in range(n):
			if k<=(n-1)//2:
				l+=1
				a[k]=l
			elif k>(n-1)//2:
				l-+1
				a[k]=l
		# print(n)
		# print(a)
		return "".join([(("*" * (i*2-1))+"\n").rjust(i+(n+1)//2) for i in a])
	else: return None

    if n > 0 and n % 2 == 1:
        return ''.join(' ' * abs((n/2) - i) + '*' * (n - abs((n-1) - 2 * i)) + '\n' for i in range(n))
    return None

    if not n%2 or n<1: return None
    d = [" "*i+"*"*(n-2*i)+"\n" for i in range(n/2,0,-1)]
    return ''.join(d) + "*"*n + "\n" + ''.join(d[::-1])



b=diamond(1)
c=diamond(2)
d=diamond(3)
e=diamond(5)
f=diamond(0)
g=diamond(-3)
print(b,c,d,e,f,g)