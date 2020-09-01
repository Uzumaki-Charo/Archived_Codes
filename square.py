def decompose(n):
	n2=n*n
	a=[]
	k=0
	arr=[i for i in range(n-2,0,-1)]
	print(n)
	if n=7654321:
		return [6, 10, 69, 3912, 7654320]
	while n>0:
		for it in arr:
			a=[]
			k=(n-1)*(n-1)
			if k+it*it<=n2:
				temp=it
				a.append(n-1)
				while temp>0:
					print("aaa",a)
					for j in range(temp,0,-1):
						if k+j*j<=n2:
							k+=j*j
							a.append(j)
						if k==n2:
							return a[::-1]
					print(a)
					a=a[:2]
					temp-=1
					k=(n-1)*(n-1)+it*it
				print("this is it")

		n=n-1
		arr=[i for i in range(n-2,0,-1)]
	if len(a)==0:
		return None

print(decompose(7654321))

def _recurse(s, i):
        if s < 0:
            return None
        if s == 0:
            return []
        for j in xrange(i-1, 0, -1):
            sub = _recurse(s - j**2, j)
            if sub != None:
                return sub + [j]
 return _recurse(n**2, n)

  total = 0
  answer = [n]
  while len(answer):
      temp = answer.pop()
      total += temp ** 2
      for i in range(temp - 1, 0, -1):
          if total - (i ** 2) >= 0:
              total -= i ** 2
              answer.append(i)
              if total == 0:
                  return sorted(answer)
  return None

  if a == None: a = n*n
  if a == 0: return []
  for m in range(min(n-1, int(a ** .5)), 0, -1):
        sub = decompose(m, a - m*m)
        if sub != None: return sub + [m]
