class NumberOfAtoms(object):

    def countOfAtoms(self, formula):

        import re
        from collections import defaultdict

        tokens = list(filter(lambda c: c, re.split('([A-Z]{1}[a-z]?|\(|\)|\d+)', formula)))

        stack, counter = [defaultdict(int)], 0

        while counter < len(tokens):
            token = tokens[counter]
            if token == '(':
                stack.append(defaultdict(int))
            else:
                count = 1
                # Check if next token is a number.
                if counter + 1 < len(tokens) and re.search('^\d+$', tokens[counter + 1]):
                    count, counter = int(tokens[counter + 1]), counter + 1
                atoms = stack.pop() if token == ')' else { token: 1 }
                # Combine counts of atoms.
                for atom in atoms:
                    stack[-1][atom] += atoms[atom] * count
            counter += 1
        return ''.join([atom + (str(count) if count > 1 else '') for atom, count in sorted(stack[-1].items())])

from nose.tools import assert_equals, assert_raises

class TestNumberOfAtoms(object):

  def testNumberOfAtoms(self):
    numberOfAtoms = NumberOfAtoms()

    assert_equals(numberOfAtoms.countOfAtoms("H2O"), "H2O")

    assert_equals(numberOfAtoms.countOfAtoms("Mg(OH)2"), "H2MgO2")

    assert_equals(numberOfAtoms.countOfAtoms("K4(ON(SO3)2)2"), "K4N2O14S4")

    print ("All test cases passed!")


def main():
  testNumberOfAtoms = TestNumberOfAtoms()
  testNumberOfAtoms.testNumberOfAtoms()

if __name__ == '__main__':
  main()
