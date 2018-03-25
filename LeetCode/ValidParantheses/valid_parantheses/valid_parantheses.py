class Stack(object):

  def __init__(self):
    self.stack = list()

  def push(self, data):
    self.stack.append(data)

  def pop(self):
    try:
      return self.stack.pop()
    except:
      raise ValueError

  def peek(self):
    try:
      return self.stack[-1]
    except:
      raise ValueError

  def length(self):
    return len(self.stack)

  def is_empty(self):
    return self.length() == 0

class ValidParantheses(object):

  def is_valid(self, parantheses):
    parantheses_stack = Stack()

    for character in parantheses:
      if (character in ['(', '{', '[']):
        parantheses_stack.push(character)
      elif (character in [')', '}', ']']):
        try: 
            stack_character = parantheses_stack.pop()
        except ValueError:
            return False
        if not((stack_character == '(' and character == ')') or
          (stack_character == '{' and character == '}') or
          (stack_character == '[' and character == ']')):
          return False
      else:
        raise ValueError
    if parantheses_stack.is_empty():
      return True
    return False


from nose.tools import assert_equal, assert_raises

class TestValidParantheses(object):

  def test_valid_parantheses(self):
    valid_parantheses = ValidParantheses()

    assert_equal(valid_parantheses.is_valid("("), False)

    assert_equal(valid_parantheses.is_valid("}"), False)

    assert_equal(valid_parantheses.is_valid("()"), True)

    assert_equal(valid_parantheses.is_valid("()[]{}"), True)

    assert_equal(valid_parantheses.is_valid("([})"), False)

    print ('All test cases passed')


def main():
  test_valid_parantheses = TestValidParantheses()
  test_valid_parantheses.test_valid_parantheses()

if __name__ == '__main__':
  main()