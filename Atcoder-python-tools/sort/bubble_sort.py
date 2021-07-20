def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                change = True
    return arr

arr = [3, 5, 2, 11, 6, 8, 1, 2]
arr = bubble_sort(arr)
print(arr)