import array
def friend(x):
    #Code
    #print(len(x))
    y=[]
    for v in x:
    	#print(v,len(v))
    	if len(v)!=4:
    		y.append(v) 
    #print(y)
    return [item for item in x if item not in y]

    return [i for i in x if len(i)==4]

k=friend(["Ryan", "Kieran", "Mark","123",])
a=friend(['1uC0c6n9PfSis5', 'C0yyT8BZfwKVweuCNNWB', '8Yyhgwr6nsPqWyPUz', 'kkooOuBokk', 'C0me', 'XXvX', 'BB9U5xwnvFCp7vbl', 'G3Ru3WoOhK', 'oBay'])
print(k)
b=friend(['Ryan', '123', 'Cool Man'])
print(a)
print(b)
