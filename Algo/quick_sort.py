tab1 = list([3,5,7,1,0,2,8,4])

def partition(tab, first, last):
    pivot = tab[last]
    i = first-1
    for j in range(first, last):
        if tab[j] <= pivot:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[last] = tab[last], tab[i+1]
    return i+1

def quick_sort(tab, first, last) :
    if first < last :
        p = partition(tab, first, last)
        quick_sort(tab, first, p-1)
        quick_sort(tab, p+1, last)
        print(tab1)


print('Unsorted list', tab1)
quick_sort(tab1, 0, len(tab1)-1)
print('Sorted list', tab1)
