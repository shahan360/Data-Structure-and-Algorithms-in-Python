def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less_then_pivot = [i for i in array[1:] if i <= pivot]
        greater_than_pivot = [i for i in array[1:] if i > pivot]
        return quicksort(less_then_pivot) + [pivot] + quicksort(greater_than_pivot)

# test case
print(quicksort([3, 6, 8, 10, 1, 2, 1]))