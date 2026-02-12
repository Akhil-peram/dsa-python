def maxProfit(prices:list[int]):
  min_value = float('inf')
  max_profit = 0
  for price in prices:
    if price < min_value:
      min_value = price
    elif price - min_value > max_profit:
      max_profit = price - min_value
  return max_profit

prices = [3,1,5,6,8,2,4]
print(maxProfit(prices))
