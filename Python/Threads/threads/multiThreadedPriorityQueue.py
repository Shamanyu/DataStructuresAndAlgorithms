import queue
import threading
import time

exitFlag = 0
queueLock = threading.Lock()
workQueue = queue.Queue(10)

class MyThread(threading.Thread):

    def __init__(self, threadID, name, queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.queue = queue

    def run(self):
        print ("Starting " + self.name)
        processData(self.name, self.queue)
        print ("Exiting " + self.name)

def processData(threadName, queue):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = queue.get()
            queueLock.release()
            print ("%s processing %s " % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

from nose.tools import assert_equals, assert_raises

class TestThreads(object):

  def testThreads(self):

    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    nameList = ["One", "Two", "Three", "Four", "Five"]
    threads = list()
    threadID = 1

    for threadName in threadList:
        thread = MyThread(threadID, threadName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1

    queueLock.acquire()
    for word in nameList:
        workQueue.put(word)
    queueLock.release()

    while not workQueue.empty():
        pass

    global exitFlag
    exitFlag = 1

    for thread in threads:
        thread.join()

    print ("All test cases passed!")


def main():
  testThreads = TestThreads()
  testThreads.testThreads()

if __name__ == '__main__':
  main()
