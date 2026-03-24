
Python Data structures
- List (Arrays)
- Tuples
- Dictionary (HashMap)
- Set
- Strings
### List (arrays)

```
array = [1,2,3,4,5,6,7,8,9,10]

array.append(11)

array.extend([12,13,14,15])

array.insert(16,1)

array.remove(16)


```
## Tuples
```
my_tuple = (2,4,6,8,10,12,16)
print(my_tuple[0])
# no adding in tuple
my_tuple.count(3)


```


# Algorithms
## Searching Algorithms
- Linear Search
- Binary Search
### Linear search

```
def search(arr,target):
	for i in range(len(arr)):
		if arr[i] == target:
			return i
			
array = [2,4,6,8,10,12,16]
tar = 10
print(search(array,tar))
```

### Binary search

```
def binarySearch(arr,target):
	left = 0
	right len(arr)-1
	while left < right:
		mid = left + (right -left) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
array = [3,2,1,6,9,7,11,8]
tar = 11
print(binarySearch(array,tar))
```


## Sorting Algorithms
- Bubble sort
- Quick sort
- Selection sort
- Insertion sort
- Merge sort
### Bubble Sort

```
def bubbleSort(arr: List[int]):
	n = len(arr)
	for i in range(n-1):
		for j in range(i,n-i-1):
			if arr[j] > arr[j+1]:
				arr[j] , arr[j+1] = arr[j+1],arr[j]
	return arr
```
### Quick sort

```
def quickSort(arr):
	if len(arr) <1:
		return arr
	pivot = arr[len(arr)//2]
	left = [x for x in range(len(arr)) if x < pivot ]
	middle = [x for x in range(len(arr)) if x == pivot ]
	right = [x for x in range(len(arr)) if x > pivot ]
	return quickSort(left)+middle+quickSort(right)
```

