def mergesort(arr, start, end):
    
    if end - start > 1:
        mid = (start + end)//2
        mergesort(arr, start, mid)
        mergesort(arr, mid, end)
        merge_arr(arr, start, mid, end)
 
def merge_arr(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            arr[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            arr[k] = right[j]
            j = j + 1
            k = k + 1
 
 
arr = input('Enter elements: ').split()
arr = [int(x) for x in arr]
mergesort(arr, 0, len(arr))
print('Sorted list: ', end='')
print(arr)