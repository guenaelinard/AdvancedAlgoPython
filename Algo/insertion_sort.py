tab1 = list([3,5,7,1,0,2,8,4])
tab2 = list()

def swap(tab, i, j) :
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def insertionAlgorythm() :
    n = len(tab1)
    for i in range(n) :
        temp = tab1[i]
        j = i
        while j > 0 and tab1[j-1] > temp :
            tab1[j] = tab1[j-1]
            j = j-1
        tab1[j] = temp

print('Unsorted list', tab1)
insertionAlgorythm()
print('Sorted list', tab1)