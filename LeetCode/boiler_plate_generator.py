from sys import argv
import json
import fileinput

class BoilerPlateGenerator(object):

  def getBoilerPlateCode(self):
    boilerPlateCode = """class %s(object):

  def %s(self):
    pass


from nose.tools import assert_equals, assert_raises

class %s(object):

  def %s(self):
    %s = %s()

    print ("All test cases passed!")


def main():
  %s = %s()
  %s.%s()

if __name__ == '__main__':
  main()
    """
    return boilerPlateCode

  def generateBoilerPlate(self, rawData):
    rawJsonData = json.loads(rawData)
    classNameLength = len(rawJsonData["className"])
    className = str(rawJsonData["className"][0]).capitalize()
    classMethod = str(rawJsonData["className"][0])
    for counter in range(1, classNameLength):
      className += str(rawJsonData["className"][counter]).capitalize()
      classMethod += str(rawJsonData["className"][counter]).capitalize()
    testClassName = 'Test'+className
    testClassMethod = 'test'+classMethod[0].upper()+classMethod[1:]
    boilerPlateCode = self.getBoilerPlateCode()
    print (boilerPlateCode % (className, classMethod, 
      testClassName, testClassMethod, classMethod, className,
      testClassMethod, testClassName, testClassMethod, testClassMethod))

def main(fileInput):
  boilerPlateGenerator = BoilerPlateGenerator()
  boilerPlateGenerator.generateBoilerPlate(fileInput)

if __name__ == '__main__':
  main(''.join(fileinput.input()))