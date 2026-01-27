def reverse(list):
    n = len(list)
    left = 0
    right = n - 1
    while left < right:
        list[left], list[right] = list[right], list[left]
        left += 1
        right -= 1
    return list

ls = [1, 2, 3, 4, 5]
print(reverse(ls)) 