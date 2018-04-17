class firstn(object):

    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, list()

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            current, self.num = self.num, self.num+1
            return current
        else:
            raise StopIteration()

print(sum(firstn(10)))
