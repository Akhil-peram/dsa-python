def MaxSubArray(arr:list['int']):
  current_sum = arr[0]
  max_sum = arr[0]
  for num in arr:
    current_sum = max(num,current_sum+num)
    max_sum = max(max_sum,current_sum)
  return max_sum

# kadanes Algorithm 
"""
its the sum of sub arrays 
Kadanes analogy 
if current sum is equal to negative start fresh 
# 1 to 6 sum it = 11 and -1 , current sum = 10 move  forward and do the same. and if 
the current sum is negative drop the negative at arr[0] and store the next num in current sum
like in [1,4,6,-1,2,-3,-2,5]
sum all positives = [1,4,6,5,2]
and negatives = [-1,-3,-2]
positives = 18 
negatives = -6
total = 12
"""
