#Majd El-Tahan 101037041
dicti = {}
def countsort (list):
    dicti = {}
    for i in list:
        if i in dicti:
            dicti[i] +=1
        else:
            dicti[i][i] = 1
    x=sorted(dicti)
    for i in x:
        sorted_list = []
        for j in range(0,dicti[i]):
            sorted_list.append(i)
