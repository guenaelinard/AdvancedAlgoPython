tab1 = list([3,5,7,1,0,2,8,4])
tab2 = list()

def swap(tab, i, j) :
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def shell_sort():
    length = len(tab1)
    n = 0
    while n < int(length/3) :
        n = 3*n+1   #Ceci est le gap

    while n > 0 :
        for i in range(n, length) :
            value = tab1[i]
            j = i
            while j> n-1 and tab1[j-n] > value :
                swap(tab1, j, j-n)
                print(tab1)
                j = j-n
            print(tab1)
        n = int((n-1)/3)
    print(tab1)

print('Unsorted list', tab1)
shell_sort()
print('Sorted list', tab1)


