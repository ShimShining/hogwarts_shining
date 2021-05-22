# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/22
Describe:链表
"""


class SingleLinkedList:

    def __init__(self):

        self.head = None

    def insert_tail(self, data):

        new_node = self.Node(data)
        # 头结点为空,链表为空,直接插入到头结点
        if self.head is None:
            self.head = new_node
            return
        # 链表不为空,从头结点遍历找尾结点
        q = self.head
        while q.next is not None:
            q = q.next
        # 将插入的值赋给尾结点
        q.next = new_node

    def insert_to_head(self, data):

        new_node = self.Node(data)
        # 链表为空,直接赋值给头结点
        if self.head is None:
            self.head = new_node
            return
        # 链表不为空,将插入到头的新结点的next指向原头结点
        new_node.next = self.head
        # 将头结点指向新插入的结点
        self.head = new_node

    def delete_by_value(self, data):

        # 如果链表为空,直接返回false
        if self.head is None:
            return False
        p = self.head
        q = None
        # 遍历链表,结束条件为结点的值=data
        while p is not None and p.data != data:
            q = p
            p = p.next
        # 循环到结尾,也没找到值=data的结点,返回false
        if p is None:
            return False
        # 头结点的值=data,直接将头结点指向next,完成删除
        if q is None:
            self.head = self.head.next
        else:
            # 将要删除的结点p的前驱结点q的next指向要删除的结点的next,完成删除
            q.next = p.next
        return True

    def find_by_value(self, data):

        # 链表为空直接返回
        if self.head is None:
            return None
        p = self.head

        while p is not None and p.data != data:
            p = p.next

        # 如果data不存在链表中,p=none
        if p is None:
            return None
        # 找到对应结点
        return p

    def insert_after(self, node, value):

        insert_node = self.Node(value)
        # 如果给定的结点为空,则插入到尾结点
        if node is None:
            self.insert_tail(value)
            return
        # 插入结点的next等于node的下一个结点
        insert_node.next = node.next
        # node结点的下一个为插入结点,完成插入
        node.next = insert_node

    def insert_before(self, node, value):

        insert_node = self.Node(value)
        if self.head is None:
            self.insert_to_head(value)
            return
        p = self.head
        while p is not None and p.next != node:
            p = p.next
        if p is None:
            return
        p.next = insert_node
        insert_node.next = node

    def print_all(self):

        # 遍历链表并打印值
        p = self.head
        # 链表为空直接返回
        if p is None:
            return
        # 从头结点开始遍历不为空的结点
        while p is not None:
            print(p.data)
            p = p.next

    class Node:

        def __init__(self, data):

            self.data = data
            self.next = None


def test_link():
    link = SingleLinkedList()
    data = [1, 2, 5, 3, 1]
    for i in data:
        link.insert_tail(i)
    link.insert_to_head(99)
    # 打印内容为 99 1 2 5 3 1
    link.print_all()
    link.delete_by_value(2)
    assert not link.delete_by_value(999)
    assert link.delete_by_value(99)
    # 打印内容为 1 5 3 1
    link.print_all()
    assert link.find_by_value(2) is None
    new_node = link.find_by_value(3)
    link.insert_after(new_node, 10)
    assert link.find_by_value(3).next.data == 10
    link.insert_before(new_node, 30)
    assert link.find_by_value(5).next.data == 30