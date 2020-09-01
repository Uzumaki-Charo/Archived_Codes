def longest_palindrome (s):
    # Your code goes in here
    #
    #print(len(s))
    o=0
    h=0
    s=s.replace(" ","")
    #print(s)
    #print(len(s))
    max=-1
    if len(s)==1:
    	return 1
    elif len(s)==0:
    	return 0
    for i in range(0,len(s)):
    	for j in range(len(s)-1,i,-1):
    		if s[i]==s[j]:
    			m=0
    			k=s[i:j+1]
    			for n in range(len(k)//2):
    				if k[n]==k[-n-1]:
    					m+=2
    			if m==len(k)-1:
    				m+=1
    			if m>max and m==len(k):
    				max=m
    				o=len(k)
    if max==o:
    	return max
    elif max!=o:
    	return 1
    else: return m

    return max((n for n in range(len(s), 0, -1) for i in range(len(s)-n+1) if s[i:i+n] == s[i:i+n][::-1]), default=0)

    for i in range(len(s), 0, -1):
        for j in range(len(s)-i+1):
            sub = s[j:j+i]
            if sub == sub[::-1]:
                return i
    return 0

    longest = 0
    for left in xrange(len(s)):
        for right in xrange(len(s), left, -1):
            if s[left:right] in (s[left:right])[::-1]:
                longest = max(right-left, longest)
                break
    return longest


k=longest_palindrome("abcdefghba")
print(k)