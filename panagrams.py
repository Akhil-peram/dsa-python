def isPanagram(s:str):
  return True if set('abcdefghijklmnopqrstuvwxyz').issubset(s.lower()) else False

sentence = "The quick brown fox jumps over the lazy dog "

print(isPanagram(sentence))

"""

a string line or a sentence is panagram if all the alphabets exist in the string 

otherwise not a panagram 

"""
