import math
class SecureList(list):
    def __getitem__(self, key):
        ret = list(self)[key]
        del self[key]
        return ret
    def __repr__(self):
        ret = list(self).__repr__()
        del self[:]
        return ret
    def __str__(self):
        ret = list(self).__str__()
        del self[:]
        return ret
		
class SecureList():
  # Implement here...
  def __init__(self, list):
      self.list = list[:]

  def __getitem__(self, index):
    return (self.list).pop(index)

  def __str__(self):
    temp, self.list = self.list, [] 
    return str(temp)  

  def __repr__(self):
    temp, self.list = self.list, []
    return repr(temp)

  def __len__(self):
      return len(self.list)