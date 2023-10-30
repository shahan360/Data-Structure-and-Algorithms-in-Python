def bubbleSort(l2):
    for i in range(0,len(l2)-1):
        temp = 0
        isSorted = 1
        for j in range(0,len(l2)-i-1):
            if l2[j]>l2[j+1]:
                temp = l2[j+1]
                l2[j+1]=l2[j]
                l2[j]=temp
                isSorted = 0
    if (isSorted==1):
        print("list is not sorted")
    return l2                

# l1 = [31,42,10,9,56,38,4]

l1 = [1,2,3,5,4]

print("UnSorted List is",l1)
l2 = bubbleSort(l1)
print("Sorted List is",l2)