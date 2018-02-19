from collections import OrderedDict

class Node(object):

    def __init__(self, key, parent=None, terminates=False):
        self.key = key
        self.parent = parent
        self.terminates = terminates
        self.children = OrderedDict()

class Trie(object):

    def __init__(self):
        self.root = Node('')

    # Time complexity: O(m); where m is the length of the word
    # Space complexity: O(h); for the recursion depth
    def find(self, word):
        if word is None:
            # raise TypeError('Word cannot be none')
            return None
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node if node.terminates else None

    # Time complexity: O(m); where m is the length of the word
    # Space complexity: O(h); for the recursion depth
    def insert(self, word):
        if word is None:
            # raise TypeError('Word cannot be none')
            return None
        node = self.root
        parent = None
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = Node(char, parent=node)
                node = node.children[char]
        node.terminates = True

    # Time complexity: O(m+h); where m is the length of the word and h is tree height
    # Space complexity: O(h); for the recursion depth
    def remove(self, word):
        if word is None:
            # raise TypeError('Word cannot be none')
            return None
        node = self.find(word)
        if node is None:
            # raise KeyError('Word does not exist')
            return None
        node.terminates = False
        parent = node.parent
        while parent is not None:
            if node.children or node.terminates:
                return
            del parent.children[node.key]
            node = parent
            parent = parent.parent

    # Time complexity: O(n); where n is the number of nodes
    # Space complexity: O(h); for the recursion depth
    def list_words(self):
        result = list()
        current_word = ''
        self._list_words(self.root, current_word, result)
        return result

    def _list_words(self, node, current_word, result):
        if node is None:
            return
        for key, child in node.children.items():
            if child.terminates:
                result.append(current_word + key)
            self._list_words(child, current_word + key, result)


# %load test_trie.py
from nose.tools import assert_true

class TestTrie(object):

    def test_trie(self):
        print('Test: Remove from empty trie')
        trie = Trie()
        assert_true(trie.remove('foo') is None)

        print('Test: Insert')
        words = ['a', 'at', 'has', 'hat', 'he',
                 'me', 'men', 'mens', 'met']
        for word in words:
            trie.insert(word)
        for word in trie.list_words():
            assert_true(trie.find(word) is not None)

        # Remove me
        # Remove mens
        # Remove a
            
        print('Test: Remove me')
        trie.remove('me')
        words_removed = ['me']
        words = ['a', 'at', 'has', 'hat', 'he',
                 'men', 'mens', 'met']
        for word in words:
            assert_true(trie.find(word) is not None)
        for word in words_removed:
            assert_true(trie.find(word) is None)

        print('Test: Remove mens')
        trie.remove('mens')
        words_removed = ['me', 'mens']
        words = ['a', 'at', 'has', 'hat', 'he',
                 'men', 'met']
        for word in words:
            assert_true(trie.find(word) is not None)
        for word in words_removed:
            assert_true(trie.find(word) is None)

        print('Test: Remove a')
        trie.remove('a')
        words_removed = ['a', 'me', 'mens']
        words = ['at', 'has', 'hat', 'he',
                 'men', 'met']
        for word in words:
            assert_true(trie.find(word) is not None)
        for word in words_removed:
            assert_true(trie.find(word) is None)

        print('Test: Remove has')
        trie.remove('has')
        words_removed = ['a', 'has', 'me', 'mens']
        words = ['at', 'hat', 'he',
                 'men', 'met']
        for word in words:
            assert_true(trie.find(word) is not None)
        for word in words_removed:
            assert_true(trie.find(word) is None)

        print('Success: test_trie')


def main():
    test = TestTrie()
    test.test_trie()


if __name__ == '__main__':
    main()