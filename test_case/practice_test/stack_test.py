# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/20
Describe:栈
"""


class ArrayStack:

    def __init__(self, capacity):

        self.n = capacity
        self.data = [0] * capacity
        self.count = 0

    def push(self, value):

        if self.count == self.n:
            return False
        self.data[self.count] = value
        self.count += 1
        return True

    def pop(self):

        if self.count == 0:
            return None
        self.count -= 1
        return self.data[self.count]


def test_stack():
    array_stack = ArrayStack(5)
    data = ["a", "b", "c", "d", "e"]
    for i in data:
        array_stack.push(i)

    result = array_stack.push("a")
    assert not result
    data.reverse()
    for i in data:
        assert i == array_stack.pop()

    assert array_stack.pop() is None


class StackBasedOnLinkedList:

    def __init__(self):
        self.top = None

    def push(self, value):

        new_node = self.Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):

        if self.top is None:
            return -1
        value = self.top.value
        self.top = self.top.next
        return value

    class Node:

        def __init__(self, value):
            self.value = value
            self.next = None


def test_static():
    stack = StackBasedOnLinkedList()
    data = [1, 2, 3, 4, 5]
    for i in data:
        stack.push(i)
    data.reverse()
    for i in data:
        assert i == stack.pop()
    assert stack.pop() == -1

