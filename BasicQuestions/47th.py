def isReverse(word1, word2):

  print("First Word = ", word1)
  print("Second Word = ", word2)

  if word1 == word2[1]:
    return True
  else:
    return False

x = isReverse("Hello", "olleh")
print(x, x)
