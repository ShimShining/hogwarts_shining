# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/20
Describe:队列
普通队列
优化队列
循环队列
链式队列
"""


class CommonQueue:

    def __init__(self, capacity):

        self.data = [0] * capacity
        self.head = 0
        self.tail = 0
        self.n = capacity

    def enqueue(self, item):

        if self.tail == self.n:
            return False
        self.data[self.tail] = item
        self.tail += 1
        return True

    def dequeue(self):

        if self.head == self.tail:
            return None
        value = self.data[self.head]
        self.head += 1
        return value


def test_common_queue():
    a = CommonQueue(10)
    a.enqueue("10")
    a.enqueue("20")
    deque_item = a.dequeue()
    assert deque_item == "10"
    a.enqueue("30")
    assert a.data[a.head] == "20"
    assert a.data[a.tail - 1] == "30"


class OptimizeQuene:

    def __init__(self, capacity):

        self.items = [0] * capacity
        self.n = capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, item):

        if self.tail == self.n:

            if self.head == 0:
                return False
            for i in range(self.head, self.tail):

                self.items[i-self.head] = self.items[i]
            self.tail = self.tail - self.head
            self.head = 0
        self.items[self.tail] = item
        self.tail += 1
        return True

    def dequeue(self):

        if self.head == self.tail:
            return None
        value = self.items[self.head]
        self.head += 1
        return value


def test_optimize_queue():
    a = OptimizeQuene(3)
    a.enqueue("10")
    a.enqueue("20")
    a.enqueue("30")
    result = a.enqueue("40")
    assert not result
    deque_item = a.dequeue()
    assert deque_item == "10"
    a.enqueue("30")
    assert a.items[0] == "20"
    assert a.items[2] == "30"


class LinkedQueue:

    def __init__(self):

        self.head = None
        self.tail = None

    def enqueue(self, node):

        if self.head is None:
            new_node = self.Node(node)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = self.Node(node)
            self.tail = self.tail.next

    def dequeue(self):

        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    class Node:

        def __init__(self, value):
            self.value = value
            self.nxt = None


def test_queue():
    a = LinkedQueue()
    a.enqueue("10")
    a.enqueue("20")
    a.enqueue("30")
    deque_item = a.dequeue()
    assert deque_item == "10"
    assert a.head.value == "20"
    assert a.head.next.value == "30"


class CircleQueue:

    def __init__(self, capacity):

        self.items = [0] * capacity
        self.n = capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, item):

        if (self.tail + 1) % self.n == self.head:
            return False
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.n
        return True

    def dequeue(self):

        if self.head == self.tail:
            return None
        value = self.items[self.head]
        self.head = (self.head + 1) % self.n
        return value


def test_queue():
    a = CircleQueue(3)
    a.enqueue("10")
    a.enqueue("20")
    result = a.enqueue("30")
    assert not result
    a.dequeue()
    a.enqueue("30")
    assert a.items[2] == "30"
    result = a.enqueue("10")
    assert not result


if __name__ == "__main__":

    test_common_queue()

