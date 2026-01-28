ls = [23,1,2,22,33,5,6,7,2,9,0,34]

def selection(arr:list[int]):
  n = len(arr)
  for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
      if arr[j]<arr[min_index]:
        min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
  return arr

print(selection(ls))
        
        
        
    
  


