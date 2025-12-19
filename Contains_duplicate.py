def contains_duplicate(input):
  """
  Return True if any value appears at least twice in the array, else return False
  
  :param input: (List) array of int values
  :return: (bool) Return True for repeated values. False if not.
  """

  for i in input:
    input.remove(i)
    if i in input:
      return True
    else:
      return False

result = contains_duplicate([1,3,5,7,1])
print(result)