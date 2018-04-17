# You have a large list of names, which you have to read five at a time
# and reverse each name in place. The five names will be processed using parallel threads.

import queue
import threading
import time

exitFlag = 0
queueLock = threading.Lock()

class WorkQueue(object):

    def __init__(self, taskLimit=100):
        self.taskLimit = taskLimit
        self.tasksCreated = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.tasksCreated < self.taskLimit:
            self.tasksCreated += 1
            return 'Shubham'
        else:
            raise StopIteration()

    def getWork(self):
        return self.next()

    def isEmpty(self):
        return self.tasksCreated >= self.taskLimit

    def __str__(self):
        return "WorkQueue"

class MyThread(threading.Thread):

    def __init__(self, threadID, threadName, taskQueue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName
        self.taskQueue = taskQueue

    def run(self):
        processData(self.threadName, self.taskQueue)

def processData(threadName, taskQueue):
    while not exitFlag:
        queueLock.acquire()
        if not taskQueue.isEmpty():
            # work = next(taskQueue)
            work = taskQueue.getWork()
            queueLock.release()
            print (threadName + " working on task ", work)
        else:
            queueLock.release()

class Rizort2Redo(object):

    def rizort2Redo(self):

        workQueue = WorkQueue(5)

        consumerThreadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5"]
        consumerThreads = list()
        consumerThreadID = 1

        for threadName in consumerThreadList:
            thread = MyThread(consumerThreadID, threadName, workQueue)
            thread.start()
            consumerThreads.append(thread)
            consumerThreadID += 1

        while not workQueue.isEmpty():
            pass

        global exitFlag
        exitFlag = 1

        for thread in consumerThreads:
            thread.join()

from nose.tools import assert_equals, assert_raises

class TestRizort2Redo(object):

  def testRizort2Redo(self):
    rizort2Redo = Rizort2Redo()

    rizort2Redo.rizort2Redo()

    print ("All test cases passed!")


def main():
  testRizort2Redo = TestRizort2Redo()
  testRizort2Redo.testRizort2Redo()

if __name__ == '__main__':
  main()
