arr = [1, 2, 3, 4, 5]
max_index, min_index = arr.index(max(arr)), arr.index(min(arr))
arr[max_index], arr[min_index] = arr[min_index], arr[max_index]
print(arr)
