# https://www.hackerearth.com/fr/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/mancunian-and-fantabulous-pairs/

class Stack(object):

  def __init__(self):
    self.elements = list()

  def push(self, element):
    self.elements.append(element)

  def pop(self):
    try:
      return self.elements.pop()
    except:
      return None

  def top(self):
    try:
      return self.elements[-1]
    except:
      return None

class MancunianAndFantabulousPairs(object):

  def __init__(self):
    pass

  def get_user_input(self):
    N = int(input())
    data = [int(number) for number in input().split()]
    self.set_input(N, data)

  def set_input(self, N, data):
    self.N = N
    self.data = data
    self.stack = Stack()

  def get_distinct_fantabulous_pairs(self):
    count = 0
    for number in self.data:
      while self.stack.top() != None and self.stack.top() < number:
        self.stack.pop()
        count += 1
      self.stack.push(number)
    return count

if __name__ == '__main__':
  mancunian_and_fantabuluous_pairs = MancunianAndFantabulousPairs()
  mancunian_and_fantabuluous_pairs.get_user_input()
  print (mancunian_and_fantabuluous_pairs.get_distinct_fantabulous_pairs())