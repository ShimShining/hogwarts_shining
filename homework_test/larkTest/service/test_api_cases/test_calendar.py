# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/1
Describe: 日历测试
"""
import time

from homework_test.larkTest.service.api.calendar import Calendar


class TestCalendar:

    def setup_class(self):

        self.calendar = Calendar()

    def teardown_class(self):

        pass

    def test_get_calendar_lists(self):

        summary = "Lark接口日历自动化" + str(int(time.time()))
        c = self.calendar.create(summary, permissions='public')
        calendar_lists = self.calendar.get_lists()
        assert len(calendar_lists) > 0

    def test_get_no_calendar_lists(self):

        self.calendar.delete_all()
        calendar_lists = self.calendar.get_lists()
        assert len(calendar_lists) == 1

    def test_create_calendar(self):

        summary = "Lark接口日历自动化" + str(int(time.time()))
        c = self.calendar.create(summary, permissions='public')
        assert c["code"] == 0
        assert c["data"]['calendar']["summary"] == summary

    def test_update_calendar(self):

        pass

    def test_delete_calendar(self):

        summary = "Lark接口日历自动化删除" + str(int(time.time()))
        self.calendar.create(summary, permissions='public')
        befor_c_len = len(self.calendar.get_calendar_ids())
        self.calendar.delete()
        after_c_len = len(self.calendar.get_calendar_ids())
        assert after_c_len == befor_c_len - 1

    def test_delete_calendar_by_summary(self):

        summary = "Lark接口日历自动化删除" + str(int(time.time()))
        self.calendar.create(summary, permissions='public')
        befor_c_len = len(self.calendar.get_calendar_ids())
        self.calendar.delete_by_summary(summary)
        after_c_len = len(self.calendar.get_calendar_ids())
        assert after_c_len == befor_c_len - 1
        assert not self.calendar.get_calendar_id_by_summary(summary)

    def test_get_one_calendar(self):

        summary = "Lark日历AT获取1条" + str(int(time.time()))
        self.calendar.create(summary, permissions='public')
        j = self.calendar.get(summary)
        assert j["data"]["summary"] == summary


