tab1 = list([3,5,7,1,0,2,8,4])

def swap(tab, i, j) :
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def bubble_sort():
    n = len(tab1)
    passage = 0
    permute = True
    while permute:
        permute = False
        for i in range(n-1):
            if tab1[i] > tab1[i+1]:
                temp = tab1[i]
                tab1[i] = tab1[i+1]
                tab1[i+1] = temp
                permute = True
        passage = passage + 1

print('Unsorted list', tab1)
bubble_sort()
print('Sorted list', tab1)