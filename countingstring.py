

def XO(string):
	array=[0,0]
	string=string.lower()
	for i in range(0,len(string)):
		if string[i]=="o":
			array[0]+=1
		elif string[i]=="x":
			array[1]+=1
	if array[0]==array[1]:
		return True
	else: return False
def xo(string):
	return string.lower().count("o")==string.lower().count("x")


a=xo("ooxx")
b=xo("xoXoo")
c=xo("XxooxO")
print(a,b,c)

# s="ooxoXO"
# s=s.lower()
# if s[2]==s[4]:
# 	print (True)
# else: print (False)
# print(len(s))