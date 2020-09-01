	

def pic():
	picture = [
	[0,0,0,1,0,0,0],
	[0,0,1,1,1,0,0],
	[0,1,1,1,1,1,0],
	[1,1,1,1,1,1,1],
	[0,0,0,1,0,0,0],
	[0,0,0,1,0,0,0]
	]

	l = len(picture[0])
	m = len(picture)

	for i in range(0,m):
		for j in range(0,l):
			if picture[i][j] == 0:
				print(' ',end = '')
			else:
				print('*',end = '')
		print('\n')