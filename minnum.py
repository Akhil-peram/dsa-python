def minnum(list):
    if not list:
        return None  # Return None if the list is empty
    min_value = list[0]
    for num in list:
        if num < min_value:
            min_value = num
    return min_value    

# Example usage
numbers = [3, 1, 4, 1, 5, 9 , 2, 6, 5,0]
print(minnum(numbers))