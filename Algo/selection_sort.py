tab1 = list([3,5,7,1,0,2,8,4])
tab2 = list()

def swap(tab, i, j) :
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def selectionAlgorythm() :
    while len(tab1) > 0 :
        minVal = tab1[0]
        for i in range(len(tab1)) :
            if minVal > tab1[i] :
                minVal = tab1[i]
        tab2.append(minVal)
        tab1.remove(minVal)
    print(tab2)

print('Unsorted list', tab1)
selectionAlgorythm()
print('Sorted list', tab1)