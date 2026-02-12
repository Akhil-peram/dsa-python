# Method 2 Brute Forcing
def twosum_brute_force(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []
arr = [2,7,11,16]
target = 9
print(twosum_brute_force(arr,target))
