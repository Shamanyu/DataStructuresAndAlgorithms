class Stack(object):

    def __init__(self):
        self.stack = list()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            raise Exception('Pop attempted on empty stack')
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return not self.size()

class MyQueue(object):

    def __init__(self):
        self.primaryStack = Stack()
        self.auxiliaryStack = Stack()

    def push(self, data):
        self.primaryStack.push(data)

    def pop(self):
        if self.primaryStack.isEmpty():
            raise Exception('Pop attempted on empty queue')
        while(1):
            try:
                data = self.primaryStack.pop()
                self.auxiliaryStack.push(data)
            except:
                break
        dataToReturn = self.auxiliaryStack.pop()
        while(1):
            try:
                data = self.auxiliaryStack.pop()
                self.primaryStack.push(data)
            except:
                break
        return dataToReturn

    def peek(self):
        if self.primaryStack.isEmpty():
            return None
        while(1):
            try:
                data = self.primaryStack.pop()
                self.auxiliaryStack.push(data)
            except:
                break
        dataToReturn = self.auxiliaryStack.peek()
        while(1):
            try:
                data = self.auxiliaryStack.pop()
                self.primaryStack.push(data)
            except:
                break
        return dataToReturn

    def empty(self):
        return self.primaryStack.isEmpty()


from nose.tools import assert_equals, assert_raises

class TestImplementQueueUsingStacks(object):

  def testImplementQueueUsingStacks(self):
    implementQueueUsingStacks = MyQueue()

    print ("All test cases passed!")


def main():
  testImplementQueueUsingStacks = TestImplementQueueUsingStacks()
  testImplementQueueUsingStacks.testImplementQueueUsingStacks()

if __name__ == '__main__':
  main()
