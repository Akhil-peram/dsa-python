def missingNumber(self, nums: List[int]) -> int:
        actual_sum = 0
        n = len(nums)
        sum_of_n = n * (n + 1) // 2
        actual_sum = sum(nums)
        return sum_of_n - actual_sum
