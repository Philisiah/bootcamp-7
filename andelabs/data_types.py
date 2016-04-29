def data_type(x=None):
  '''
  function takes in an argument and returns results based on the data type
  '''
  if type(x) == str:
    return len(x)
  elif x == None:
    return 'no value'
  elif type(x) == bool:
    return x
  elif type(x) == int:
    if x < 100:
      return 'less than 100'
    else:
      return 'more than 100'
  elif type(x) == list:
    if len(x) >= 3:
      return x[2]
    else:
      return None
 
