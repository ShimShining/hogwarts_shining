# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/24
Describe:饿汉式单例;懒汉式单例
"""
from threading import Lock


class HungryIdMaker:

    __instance = None
    __id = -1

    def __new__(cls):

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def get_id(self):

        self.__id += 1
        return self.__id


def test_hungry_id_maker():

    # IdMaker 是单例类，只允许有一个实例

    a = HungryIdMaker()
    b = HungryIdMaker()
    c = HungryIdMaker()

    id1 = a.get_id()

    id2 = b.get_id()

    id3 = c.get_id()

    print(id1, id2, id3)
    assert id(a) == id(b)
    assert id(b) == id(c)


class LazyIdMaker:

    __instance = None
    __id = 1
    __instance_lock = Lock()

    def __new__(cls):
        pass

    @classmethod
    def get_instance(cls):
        # 避免多线程同时创建多个实例,创建的时候加锁
        with cls.__instance_lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
        return cls.__instance

    def get_id(self):
        self.__id += 1
        return self.__id


def test_lazy_id_maker():

    # IdMaker 是单例类，只允许有一个实例

    a = LazyIdMaker.get_instance()
    b = LazyIdMaker.get_instance()
    c = LazyIdMaker.get_instance()

    id1 = a.get_id()

    id2 = b.get_id()

    id3 = c.get_id()

    print(id1, id2, id3)
    assert id(a) == id(b)
    assert id(b) == id(c)


if __name__ == "__main__":

    test_lazy_id_maker()
    test_hungry_id_maker()





