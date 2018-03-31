class DependencyMatrix(object):

    def __init__(self, id):
        self.id = id
        self.numberOfDependencies = 0
        self.dependentOn = set()

class CourseSchedule(object):

  def courseSchedule(self, numCourses, prerequisites):
    self.dependencies = dict()
    for counter in range(numCourses):
        self.dependencies[counter] = DependencyMatrix(counter)
    for counter, prerequisite in enumerate(prerequisites):
        self.dependencies[prerequisite[0]].dependentOn.add(prerequisite[1])
        self.dependencies[prerequisite[0]].numberOfDependencies += 1
    while self.dependencies:
        


from nose.tools import assert_equals, assert_raises

class TestCourseSchedule(object):

  def testCourseSchedule(self):
    courseSchedule = CourseSchedule()

    assert_equals(courseSchedule.courseSchedule(2, [[1, 0]]), True)

    assert_equals(courseSchedule.courseSchedule(2, [[1, 0], [0, 1]]), False)

    print ("All test cases passed!")


def main():
  testCourseSchedule = TestCourseSchedule()
  testCourseSchedule.testCourseSchedule()

if __name__ == '__main__':
  main()
