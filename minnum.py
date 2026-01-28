def minnum(arr:list[int]):
    if not arr:
        return None  # Return None if the list is empty
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value    

# Example usage
numbers = [3, 1, 4, 1, 5, 9 , 2, 6, 5,0]

print(minnum(numbers))
