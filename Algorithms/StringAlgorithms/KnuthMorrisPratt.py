class KnuthMorrisPratt(object):

  def __init__(self):
    self.set_input(list(), list())

  def get_user_input(self):
    self.string = list(input())
    self.word = list(input())
    self.set_input(string, word)

  def set_input(self, string, word):
    self.string = string
    self.word = word
    self.construct_partial_match_table(word)

  def construct_partial_match_table(self, word):
    pos = 1
    cnd = 0

    self.partial_match_table = [-1 for counter in range(0, len(self.word))]

    while (pos < len(self.word)):
      if self.word[pos] == self.word[cnd]:
        self.partial_match_table[pos] = self.partial_match_table[cnd]
        pos = pos+1
        cnd = cnd+1
      else:
        self.partial_match_table[pos] = cnd
        cnd = self.partial_match_table[cnd]
        while cnd >= 0 and self.word[pos] != self.word[cnd]:
          cnd = self.partial_match_table[cnd]
        pos = pos+1
        cnd = cnd+1
    # self.partial_match_table[pos] = cnd

  def kmp(self):
    m = 0
    i = 0
    while (m+i < len(self.string)):
      if self.word[i] == self.string[m+i]:
        i = i+1
        if (i == len(self.word)):
          return m
          # m = m + i - self.partial_match_table[i]
          # i = self.partial_match_table[i]
      else:
        if (self.partial_match_table[i] > -1):
          m = m + i - self.partial_match_table[i]
          i = self.partial_match_table[i]
        else:
          m = m + i + 1
          i = 0
    return -1

knuth_morris_pratt = KnuthMorrisPratt()

knuth_morris_pratt.set_input('ABC ABCDAB ABCDABCDABDE', 'ABCDABD')
print (knuth_morris_pratt.kmp())