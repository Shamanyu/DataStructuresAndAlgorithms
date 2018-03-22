class LongestSubstringWithoutRepeatingCharacters(object):

  # Time complexity: O(n^2)
  # Space complexity: O(n)
  def length(self, s):
    longest_substring = list()
    current_substring = list()
    for _, item in enumerate(s):
      if (item not in current_substring):
        current_substring.append(item)
      else:
        index_of_duplicate_item = current_substring.index(item)
        current_substring = current_substring[index_of_duplicate_item+1:]
        current_substring.append(item)
      if len(current_substring) > len(longest_substring):
        longest_substring = current_substring
    return len(longest_substring)


from nose.tools import assert_equal, assert_raises

class TestLongestSubstringWithoutRepeatingCharacters(object):

  def test_longest_substring_without_repeating_characters(self):

    # Test case 1
    longest_substring_without_repeating_characters = LongestSubstringWithoutRepeatingCharacters()
    assert_equal((longest_substring_without_repeating_characters.length("abcabcbb")), 3)

    # Test case 2
    longest_substring_without_repeating_characters = LongestSubstringWithoutRepeatingCharacters()
    assert_equal((longest_substring_without_repeating_characters.length("bbbbb")), 1)

    # Test case 3
    longest_substring_without_repeating_characters = LongestSubstringWithoutRepeatingCharacters()
    assert_equal((longest_substring_without_repeating_characters.length("pwwkew")), 3)

    # Test case 4
    longest_substring_without_repeating_characters = LongestSubstringWithoutRepeatingCharacters()
    assert_equal((longest_substring_without_repeating_characters.length("shubham")), 5)

    # Test case 5
    longest_substring_without_repeating_characters = LongestSubstringWithoutRepeatingCharacters()
    assert_equal((longest_substring_without_repeating_characters.length("abcdefg")), 7)

    # Test case 6
    longest_substring_without_repeating_characters = LongestSubstringWithoutRepeatingCharacters()
    assert_equal((longest_substring_without_repeating_characters.length("aab")), 2)

    # Test case 7
    longest_substring_without_repeating_characters = LongestSubstringWithoutRepeatingCharacters()
    assert_equal((longest_substring_without_repeating_characters.length("dvdf")), 3)

    print ("All test cases passed")


def main():
  test_longest_substring_without_repeating_characters = TestLongestSubstringWithoutRepeatingCharacters()
  test_longest_substring_without_repeating_characters.test_longest_substring_without_repeating_characters()

if __name__ == '__main__':
  main()