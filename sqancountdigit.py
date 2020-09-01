def nb_dig(n, d):
    # your code
    # a=["%s"%i**2 for i in range(n+1)]
    # s=0
    # for x in a:
    # 	s+=x.count("%s"%d)
    # print(s)
    return sum(x.count("%s"%d) for x in ["%s"%i**2 for i in range(n+1)])
result=nb_dig(11011, 2)
print(result)