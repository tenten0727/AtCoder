def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr
    
    ref = arr[0]
    ref_count = 0

    for v in arr:
        if v < ref:
            left.append(v)
        elif v > ref:
            right.append(v)
        else:
            ref_count += 1

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [ref] * ref_count + right

arr = [3, 5, 2, 11, 6, 8, 1, 2]
arr = quick_sort(arr)
print(arr)
