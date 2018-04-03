class LongestCommonPrefix(object):

  def longestCommonPrefix(self, strs):
    if len(strs) == 0:
        return ''
    longestCommonPrefix = list(strs[0])
    for string in strs:
        if not string:
            return ''
        string = list(string)
        commonPrefix = list()
        counter = 0
        while(counter < len(string) and counter < len(longestCommonPrefix)):
            if longestCommonPrefix[counter] == string[counter]:
                commonPrefix.append(string[counter])
                counter += 1
            else:
                break
        longestCommonPrefix = commonPrefix
    return ''.join(longestCommonPrefix)

from nose.tools import assert_equals, assert_raises

class TestLongestCommonPrefix(object):

  def testLongestCommonPrefix(self):
    longestCommonPrefix = LongestCommonPrefix()

    print ("All test cases passed!")


def main():
  testLongestCommonPrefix = TestLongestCommonPrefix()
  testLongestCommonPrefix.testLongestCommonPrefix()

if __name__ == '__main__':
  main()
