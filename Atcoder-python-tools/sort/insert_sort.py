def insert_sort(arr):
    for i in range(1, len(arr)):
        v = arr[i]
        j = i-1
        while j >= 0 and arr[j] > v:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = v
    return arr

arr = [3, 5, 2, 11, 6, 8, 1, 2]
arr = insert_sort(arr)
print(arr)
