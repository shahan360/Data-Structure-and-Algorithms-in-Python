def insertSort(l2):
    for i in range(1,len(l2)):
        key = l2[i] 
        j = i-1
        while (j>=0 and l2[j]>key):
            l2[j+1]=l2[j]
            j-=1
        l2[j+1]=key
    return l2        
            
        

l1 = [31,42,10,9,56,38,4]

# l1 = [1,2,3,5,4]

print("UnSorted List is",l1)
l2 = insertSort(l1)
print("Sorted List is",l2)