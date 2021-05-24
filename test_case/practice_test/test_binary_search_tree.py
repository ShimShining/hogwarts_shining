# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/24
Describe:二叉查询树
"""

class BinarySearchTree:

    def __init__(self):

        self.tree = None

    def insert(self, value):

        node = self.Node(value)
        # 如果树为空,直接插入到根节点
        if self.tree is None:
            self.tree = node
            return
        # 树不为空,遍历插入的位置
        p = self.tree
        while p is not None:

            if value > p.data:

                if p.right is None:
                    p.right = node
                    return
                p = p.right

            elif value < p.data:

                if p.left is None:
                    p.left = node
                    return
                p = p.left

    def find(self, value):

        p = self.tree
        while p is not None:

            if p.data > value:
                p = p.left
            elif p.data < value:
                p = p.right
            else:
                return p
        return None

    def delete(self, value):

        p = self.tree
        q = None
        while p is not None and p.data != value:

            q = p
            if value > p.data:
                p = p.right
            elif value < p.data:
                p = p.left
        # 在树中没有找到相应的节点
        if p is None:
            return
        # 要删除的节点有两个子树
        if p.left is not None and p.right is not None:
            tmp_p = p.right
            tmp_q = p
            # 查找删除节点的右子树中的最小值,并将最小值与删除的节点值替换
            while tmp_p.left is not None:
                tmp_q = tmp_p
                tmp_p = tmp_p.left
            p.data = tmp_p.data
            p = tmp_p
            q = tmp_q
        # 删除的节点是叶子节点或者只有1个子树,左或者右
        if p.left is not None:
            child = p.left
        elif p.right is not None:
            child = p.right
        else:
            child = None
        # 要删除的节点就是根节点
        if q is None:
            self.tree = child
            return
        if q.left is p:
            q.left = child
        elif q.right is p:
            q.right = child

    def pre_order(self, node):

        if node is None:
            return
        print(node.data)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):

        if node is None:
            return
        self.in_order(node.left)
        print(node.data)
        self.in_order(node.right)

    def post_order(self, node):

        if node is None:
            return

        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)

    class Node:

        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None




def test_binary_search_tree():

    binary_search_tree = BinarySearchTree()
    data = [1, 10, 20, 40, 13]
    for i in data:
        binary_search_tree.insert(i)
    binary_search_tree.pre_order(binary_search_tree.tree)
    assert 20 == binary_search_tree.find(20).data
    binary_search_tree.delete(20)
    print(binary_search_tree.find(20))
    print("+++++++++++++++++++++++")
    assert binary_search_tree.find(20) is None
    # 1 10 40 13
    binary_search_tree.pre_order(binary_search_tree.tree)
    print("-----------------------")
    # 1 10 13 40
    binary_search_tree.in_order(binary_search_tree.tree)
    print("-----------------------")
    # 13 40 10 1
    binary_search_tree.post_order(binary_search_tree.tree)


if __name__ == '__main__':
    test_binary_search_tree()