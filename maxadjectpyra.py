
import time

day=[1,2,3,4,5,6,7]
month=[1,2,3,4,5,6,7,8,9,10,11,12]

def checkifsunday(i,sun,year):
	if month[i]==4 or month[i]==6 or month[i]==9 or month[i]==11:
		if sun<30:
			sun=sun+7
		if sun%30==1:
			return True
		else: return False
	elif month[i]==2:
		if year%4==0:
			if sun<29:
				sun=sun+7
			if sun%29==1:
				return True
			else: return False
		else:
			if sun<28:
				sun=sun+7
			if sun%28==1:
				return True
			else: return False
	else:
		if sun<31:
			sun=sun+7
		if sun%31==1:
			return True
		else: return False

def moveback(i,days,year):
	if month[i]==4 or month[i]==6 or month[i]==9 or month[i]==11:
		if days<30:
			days=days+7
		#print("case 1",days%30)
		return days%30
	elif month[i]==2:
		if year%4==0:
			if days<29:
				days=days+7
			return days%29
		else:
			if days<28:
				days=days+7			
			#print("case `2",days%28)
			return days%28
	else:
		if days<31:
			days=days+7
		#print("case 3",days%31)
		return days%31

def generateday(days):
	j=0
	for k in range(1901,2001):
		for i in range(0,12):
			days+=28
			if checkifsunday(i,days,k):
				#print("year",k)
				j+=1
				if k==2000 and month[i]==12:
					j=j-1
			days=moveback(i,days,k)
	return j
start=time.time()
result=generateday(6)
elapsed=time.time()-start
print("Those Sundays r %s found in %s seconds" % (result,elapsed))



