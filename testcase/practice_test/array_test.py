# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/19
Describe:数组
"""


class Array:

    def __init__(self, capacity):

        self.data = [0]*capacity
        self.count = 0
        self.n = capacity

    def insert(self, index, value):

        if self.n == self.count:
            return False

        if index < 0 or index > self.count:
            return False

        print(f"初始化数组self.data={self.data}")

        for i in range(self.count, index, -1):
            print(f"i={i}")
            self.data[i] = self.data[i-1]

        self.data[index] = value
        self.count += 1
        return True

    def find(self, index):

        if index < 0 or index >= self.count:
            return -1
        return self.data[index]

    def delete(self, index):

        if index < 0 or index >= self.count:
            return False

        for i in range(index+1, self.count):
            self.data[i-1] = self.data[i]

        self.count -= 1
        return True


def test_demo():
    array = Array(5)
    array.insert(0, 1)
    array.insert(0, 2)
    array.insert(1, 3)
    array.insert(2, 4)
    array.insert(4, 5)

    # 判断插入不成功
    assert not array.insert(0, 100)
    assert array.find(0) == 2
    assert array.find(2) == 4
    assert array.find(4) == 5
    assert array.find(10) == -1
    assert array.count == 5
    removed = array.delete(4)
    assert removed
    assert array.find(4) == -1
    removed = array.delete(10)
    assert not removed
    # 2 3 4 1 5
    assert array.data == [2, 3, 4, 1, 5]


if __name__ == '__main__':
    test_demo()


