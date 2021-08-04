for i in unsortedList:
		if i in frequency:
			frequency[i] +=1
		else:
			frequency[i] = 1
	tobeAppended = sorted(frequency)
	for i in tobeAppended:
		for j in range(0,frequency[i]):
			new_list.append(i)
