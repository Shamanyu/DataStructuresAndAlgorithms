class Node(object):

    def __init__(self, key, value, isLeaf):
        self.key = key
        self.value = value
        self.isLeaf = isLeaf
        self.children = dict()

    def addChild(self, key, Node):
        self.children[key] = Node

    def removeChild(self, key):
        try:
            del self.children[key]
        except:
            raise ValueError("Child doesn't exist")

    def getChildren(self):
        return self.children

    def getChildrenKeys(self):
        return self.children.keys()

class Trie(object):

    def __init__(self):
        self.root = Node('', '', False)

    def find(self, string):
        if string is '':
            return True
        return self._find(string, self.root)

    def _find(self, string, currentNode):
        if string is None:
            return True
        if currentNode is None:
            return False
        children = currentNode.getChildren()
        if string[0] in children:
            if len(string) == 1:
                return children[string[0]].isLeaf
            return self._find(string[1:], children[string[0]])
        return False

    def insert(self, string):
        if string is not '':
            return self._insert(string, self.root)

    def _insert(self, string, currentNode):
        if string is None:
            pass
        children = currentNode.getChildren()
        if string[0] in children:
            if len(string) == 1:
                if not children[string[0]].isLeaf:
                    children[string[0]].isLeaf = 1
            else:
                self._insert(string[1:], children[string[0]])
        else:
            if (len(string) > 1):
                newNode = Node(string[0], string[0], False)
                currentNode.addChild(string[0], newNode)
                self._insert(string[1:], newNode)
            else:
                currentNode.addChild(string[0], Node(string[0], string[0], True))

from nose.tools import assert_equals, assert_raises

class TestTrie(object):

  def testTrie(self):
    trie = Trie()

    assert_equals(trie.find(''), True)

    trie.insert('')

    assert_equals(trie.find('a'), False)

    trie.insert('a')

    assert_equals(trie.find('a'), True)

    assert_equals(trie.find('b'), False)

    trie.insert('b')

    assert_equals(trie.find('b'), True)

    assert_equals(trie.find('ab'), False)

    assert_equals(trie.find('ba'), False)

    trie.insert('ba')

    assert_equals(trie.find('ab'), False)

    assert_equals(trie.find('ba'), True)

    assert_equals(trie.find(''), True)

    assert_equals(trie.find('zyx'), False)

    trie.insert('zyx')

    assert_equals(trie.find('zyx'), True)

    assert_equals(trie.find('zy'), False)

    trie.insert('zy')

    assert_equals(trie.find('zy'), True)

    print ("All test cases passed!")


def main():
  testTrie = TestTrie()
  testTrie.testTrie()

if __name__ == '__main__':
  main()
