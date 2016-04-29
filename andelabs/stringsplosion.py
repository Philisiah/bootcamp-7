class StringSplosion(object):
  def __init__(self, lst):
    self.lst = lst
  
  def manipulate(self):
    strng = ""
    for i in range(len(self.lst)):
      strng = strng + self.lst[: i +1]
      
    return strng