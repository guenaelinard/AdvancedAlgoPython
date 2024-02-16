tab1 = list([3,5,7,1,0,2,8,4])

def merge_sort(tab) :
    n = len(tab)
    if n <= 1 :
        return tab
    else:
        mid = n//2
        left = tab[:mid]
        right = tab[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
    print(tab)
    return merge(left, right)


def merge(left, right) :
        result = []
        left_index = right_index = 0
        while left_index < len(left) and right_index < len(right) :
            if left[left_index] < right[right_index] :
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

            # while left_index < len(left):
            #     result.append(left[left_index])
            #     left_index += 1
            # while right_index < len(right):
            #     result.append(right[right_index])
            #     right_index += 1
            return result

print('Unsorted list', tab1)
merge_sort(tab1)
print('Sorted list', tab1)