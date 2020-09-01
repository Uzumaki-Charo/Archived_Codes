def sort_array(source_array):
	k=0
	for i in range(len(source_array)):
		for j in range(i+1,len(source_array)):
			if source_array[i]%2!=0 and source_array[j]%2!=0:
				if source_array[i]>source_array[j]:
					k=source_array[j]
					source_array[j]=source_array[i]
					source_array[i]=k	
	return source_array

	odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
