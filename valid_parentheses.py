def validParentheses(s:str):
  stack = []
  bracket_map = {"}":"{,")":"(","]":"["}
  for char in s:
    if char != bracket_map:
      top_element = stack.pop() if stack else '#'
      if bracket_map[char] != top_element:
        return False
    else:
        stack.append(char)
  return len(stack) == 0
