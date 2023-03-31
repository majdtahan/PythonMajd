 def commonpair(word):
	word_combo_list = {}
	if word not in word_array:
		return None
	for i in range(0,len(word_array)):
		if word_array[i] == word and i == len(word_array)-1:
			break
		elif word_array[i] ==  word and word_array[i+1] not in word_combo_list:
				word_combo_list[word_array[i+1]] = 0
	for i in range(0,len(word_array)):
		if word_array[i] == word and i == len(word_array)-1:
			break
		elif word_array[i] == word:
			word_combo_list[word_array[i+1]] +=1
	return max(word_combo_list,key=word_combo_list.get)
def countall():
	return len(word_array)
def countunique():
	check_array = []
	unique_word = 0
	word = ""
	for i in range(0,len(word_array)):
		word = word_array[i]
		if word in check_array:
			continue
		else:
			unique_word+=1
			check_array.append(word_array[i])
	return unique_word