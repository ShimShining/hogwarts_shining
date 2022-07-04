# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/18
Describe:
"""
class Singleton(object):

    _instance = None

    def __new__(cls, *args, **kwargs):

        if not cls._instance:

            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

        return cls._instance

class A(Singleton):

    def __new__(cls, *args, **kwargs):

        super(A, cls).__new__(cls, *args, **kwargs)

class B(Singleton):

    def __new__(cls, *args, **kwargs):

        super(B, cls).__new__(cls, *args, **kwargs)

class C(B):

    def __new__(cls, *args, **kwargs):

        super(B, cls).__new__(cls, *args, **kwargs)

if __name__ == '__main__':

    s1= A()

    s2= B()

if(id(s1)==id(s2)):

    print("Same")

else:

    print("Different")

