def binarysearch(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    Parameters:
    arr (list): A list of sorted elements.
    target: The element to search for in the list.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        else:
            high = mid - 1

    # Target was not found in the array
    return -1


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binarysearch(arr, target)

print(result)
