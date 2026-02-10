def quicksort(arr:list[int]):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot ]
  middle = [x for x in arr if x == pivot ]
  right = [x for x in arr if x > pivot ]
  return quicksort(left) + middle + quicksort(right)

arr = [6,2,3,1,9,1,11,10]
print(quicksort(arr))
