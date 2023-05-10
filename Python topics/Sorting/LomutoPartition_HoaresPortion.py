def lomutoPartition(arr, l, h):
    '''
    Lomuto partition is a partitioning algorithm used in quicksort to partition an array into two parts based on a pivot element.
    Set the pivot element to last element in array -> Initialize two variables i and j
    in loop, check for arr[j] <= pivot and swap them.
    After loop, swap pivot element with element at index i. -> Return i (pivot position).
    
    '''
    pivot = arr[h]
    i = l - 1

    for j in range(l, h):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]

    return i + 1


def hoarePartition(arr,l,h): #mostly used
    pivot=arr[l]
    i=l-1
    j=h+l
    while True:
        i=i+1
        while arr[i]<pivot:
            i=i+1
        j=j-1
        while arr[j]>pivot:
            j=j-1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]