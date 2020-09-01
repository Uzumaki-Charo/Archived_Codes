def longest_consec(strarr, k):
    # your code
    n=len(strarr)
    max=-1
    f=0
    g=""
    if n==0 or k>n or k<=0:
        return ""
    else:
        for i in range(0,n+1-k):
            m=len(strarr[i])
            for j in range(i+1,k+i):
                m+=len(strarr[j])
            if m>max:
                max=m
                f=i
        for x in range(f,f+k):
             g+=strarr[x]
        return g
    #return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""
                
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15))
# a=[1,4,6,2,5]
# print(a.sort()[2])
