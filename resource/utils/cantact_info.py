# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/26
Describe:
"""
from faker import Faker


class ContactInfo:

    def __init__(self):

        self.faker = Faker("zh-CN")

    def get_name(self):

        return self.faker.name()

    def get_phone_number(self):

        return self.faker.phone_number()
