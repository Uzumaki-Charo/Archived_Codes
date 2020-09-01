def likes(names):
    #your code here
    if len(names)==0:
        return 'no one likes this'
    #names=names.replace("'","").split(",")
    if len(names)==1:
        return '%s likes this'%(names[0])
    elif len(names)==2:
        return '%s and %s like this'%(names[0],names[1])
    elif len(names)==3:
        return '%s, %s and %s like this'%(names[0],names[1],names[2])
    else:
        return '%s, %s and %s others like this'%(names[0],names[1],len(names)-2)
a=likes([])
b=likes(['Peter'])
c=likes(['Jacob', 'Alex'])
d=likes(['Max', 'John', 'Mark'])
e=ikes(['Alex', 'Jacob', 'Mark', 'Max'])
print(a,b,c,d,e)

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)