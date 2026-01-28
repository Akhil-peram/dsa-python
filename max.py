def maxnum(arr:list[int]):
    if not arr:
        return None  # Return None if the list is empty
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

# Example usage
numbers = [3, 1, 4, 1, 5, 9 , 2, 6, 5]

print(maxnum(numbers))
