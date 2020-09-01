def pin(string):
	for i in range(0,len(string)):
		if 47<ord(string[i])<58:
			continue
		else: return False
	return len(string)==4 or len(string)==6
def validate(pin):
	return len(pin) in (4,6) and pin.isdigit()
a=pin("1234")
b=pin("a2655s")
print(a,b)