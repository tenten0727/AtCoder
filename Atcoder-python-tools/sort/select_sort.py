def sellect_sort(arr):
    for i, value in enumerate(arr):
        min_i = min(range(i, len(arr)), key=arr.__getitem__) #最小の値のインデックス
        arr[i], arr[min_i] = arr[min_i], arr[i]
    
    return arr

arr = [3, 5, 2, 11, 6, 8, 1, 2]
arr = sellect_sort(arr)
print(arr)