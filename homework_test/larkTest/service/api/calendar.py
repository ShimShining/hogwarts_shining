# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/9/1
Describe:日历接口
"""
from homework_test.larkTest.service.api.larkApi import LarkApi
import json


class Calendar(LarkApi):

    # 创建,更新,获取列表和单个,删除的基础path均是同一个,请求的method和参数不同
    __base_path = "/calendar/v4/calendars"
    __subscribe_path = ""
    __unsubscribe_path = ""
    __search_path = ""

    def create(self, summary, permissions="private", color=16711680):

        data = {
            "method": "POST",
            "url": self._base_url + self.__base_path,
            "json": {
                "summary": summary,
                "description": f"使用开放接口创建日历{summary}",
                "permissions": permissions,
                "color": color,
                "summary_alias": f"日历备注{summary}"
            }

        }
        j = self.lark_request(data)
        return j

    def get_lists(self):

        data = {
            "method": "GET",
            "url": self._base_url + self.__base_path
        }
        j = self.lark_request(data)
        c_lists = j["data"]["calendar_list"]
        self.logger.info(f"获取日历列表返回的calendar_list为 ==> {json.dumps(c_lists, indent=2, ensure_ascii=False)}")
        return c_lists

    def get_calendar_ids(self):

        calendar_lists = self.get_lists()
        return [c['calendar_id'] for c in calendar_lists if c["type"] != "primary"]

    def get_calendar_id_by_summary(self, summary):

        calendar_lists = self.get_lists()
        return [c['calendar_id'] for c in calendar_lists if c["type"] != "primary" and c['summary'] == summary]

    def update(self):

        pass

    def delete(self, calender_id=None):

        if calender_id is None:
            c_ids = self.get_calendar_ids()
            if not c_ids:
                self.logger.error(f"获取type不等于primary的calendar_ids为空列表{c_ids},不能进行删除操作,请先进行创建")
            calender_id = c_ids[0]

        data = {
            "method": "DELETE",
            "url": self._base_url + self.__base_path + f"/{calender_id}",
        }
        j = self.lark_request(data)
        self.logger.info(f"删除id={calender_id}的日历成功.")
        return j

    def get(self, summary, **kwargs):

        calender_id = self.get_calendar_id_by_summary(summary)[0]
        data = {
            "method": "GET",
            "url": self._base_url + self.__base_path + f"/{calender_id}",
        }

        j = self.lark_request(data)
        self.logger.info(f"获取id={calender_id}的日历成功.")
        return j

    def subscribe(self):

        pass

    def unsubscribe(self):

        pass

    def delete_all(self):

        c_ids = self.get_calendar_ids()
        for c_id in c_ids:
            self.delete(calender_id=c_id)
        self.logger.info("删除所有type非primary的日历成功.")

    def delete_by_summary(self, summary):

        c_id = self.get_calendar_id_by_summary(summary)
        if c_id:
            self.delete(calender_id=c_id[0])
            self.logger.info(f"通过summary删除summary={summary}的日历成功.")
        else:
            self.logger.error(f"获取summary={summary}的日历失败,该日历不存在,删除失败!!!")

