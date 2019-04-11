import random
from abc import ABCMeta, abstractmethod


class ReplacementStrategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert(self, cache_data, key, value):
        raise NotImplemented("Should implement 'insert'")


class RandomReplacementStrategy(ReplacementStrategy):

    def insert(self, cache_data, key, value):
        key_to_remove = random.choice(cache_data.keys())
        del cache_data[key_to_remove]
        cache_data[key] = value


class Cache(object):

    def __init__(self, capacity, replacement_strategy, read_time, write_time):
        self.capacity = capacity
        self.replacement_strategy = replacement_strategy
        self.read_time = read_time
        self.write_time = write_time
        self.data = dict()

    def read(self, key):
        if key in self.data:
            return self.data[key]
        # raise ValueError
        return None

    def write(self, key, value):
        if key in self.data:
            if self.data[key] == value:
                return 'No update'
            else:
                self.data[key] = value
                return 'Updated'
        elif len(self.data) < self.capacity:
            self.data[key] = value
            return 'Updated'
        else:
            self.replacement_strategy(self.data, key, value)


class MultiLevelCache(object):

    def __init__(self, cache_list):
        self.cache_list = cache_list

    def read(self, key):
        pass

    def write(self, key, value):
        pass


def runner():
    cache1 = Cache(2, RandomReplacementStrategy(), 1, 2)
    print (cache1.read(1))
    print (cache1.write(1, 2))
    print (cache1.read(1))


if __name__ == '__main__':
    runner()
