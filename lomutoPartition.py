l1 = [45,8,3,5,87,10]
def lomutoPart(arr,l,h):
    pivot = arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return arr 
b = lomutoPart(l1,0,5)
print(b)        