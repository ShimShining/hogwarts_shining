# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/1
Describe: 日历测试
"""
from homework_test.larkTest.service.api.calendar import Calendar


class TestCalendar:

    def setup(self):

        self.calendar = Calendar()

    def teardown(self):

        pass

    def test_get_calendar_lists(self):

        calendar_lists = self.calendar.get_lists()
        assert len(calendar_lists) > 0

    def test_get_no_calendar_lists(self):

        calendar_lists = self.calendar.get_lists()
        assert len(calendar_lists) > 0

    def test_create_calendar(self):

        pass

    def test_update_calendar(self):

        pass

    def test_delete_calendar(self):

        pass

    def test_get_one_calendar(self):

        pass


