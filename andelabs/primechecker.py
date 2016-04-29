class PrimeChecker(object):
  def __init__(self, number=None):
    self.number = number
  
  def is_prime(self):
    if len(self.number) >= 1:
      if type(self.number) == str:
        self.number = int(self.number)
  
      if self.number == 1:
        return False
      elif self.number == 3:
        return True
      if self.number > 3:
        for i in range(3, (self.number-1)):
          if self.number % i == 0:
            return False
          else:
            return True
    return False