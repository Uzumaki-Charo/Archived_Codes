
def rot13(message):
	m=''
	k=0
	for i in range(len(message)):
		print(ord(message[i]))
		if ord('a')<=ord(message[i])<=ord('z'):
			k=ord(message[i])+13
			if k>ord('z'):
				m+=chr(ord('a')+k%(ord('z')+1))
			else: m+=chr(k)
		elif ord('A')<=ord(message[i])<=ord('Z'):
			k=ord(message[i])+13
			if k>ord('Z'):
				m+=chr(ord('A')+k%(ord('Z')+1))
			else: m+=chr(k)
		else: m+=message[i]
	return m

	return ''.join(chr((65 if c.isupper() else 97) + ((ord(c) - (65 if c.isupper() else 97)) + 13)%26) if c.isalpha() else c for c in message)

rot13("test")
rot13("Test")
