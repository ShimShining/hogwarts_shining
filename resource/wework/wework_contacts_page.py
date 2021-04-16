# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/4/16
Describe:企业微信通讯录界面封装
"""
from time import sleep
import random
from test_case.base import MPath, Common, Base
from selenium import webdriver


class WeWorkContactsPage:

    def get_locator(self):

        return {
            # //*[contains(@class,"ww_operationBar")][1]//*[text()="添加成员"]
            "add_member_top": MPath('.ww_operationBar:nth-child(1) .js_add_member', "CSS_SELECTOR"),
            "add_member_bottom": MPath('//*[contains(@class,"ww_operationBar")][2]//*[text()="添加成员"]'),
            "user_name": MPath('username', 'ID'),
            "alias_name": MPath('memberAdd_english_name', 'ID'),
            "account": MPath('memberAdd_acctid', 'ID'),
            "gender_male": MPath('input[name=gender][value=1]', 'CSS_SELECTOR'),
            "gender_female": MPath('input[name=gender]:not([checked=checked])', 'CSS_SELECTOR'),
            "phone": MPath("memberAdd_phone", "ID"),
            "local_phone": MPath("memberAdd_telephone", 'ID'),
            "email": MPath('memberAdd_mail', 'ID'),
            "address": MPath('memberEdit_address', 'ID'),
            "department": MPath(".ww_groupSelBtn_item_text", "CSS_SELECTOR"),
            "modify_depart": MPath('//*[contains(@class,"ww_groupSelBtn_add") and text()="修改"]'),
            "search_depart": MPath('memberSearchInput', 'ID'),
            "choose_depart": MPath(None),
            "search_confirm": MPath('a:contains("确认")', 'CSS_SELECTOR'),
            "search_cancel": MPath('a:contains("确认")~a', 'CSS_SELECTOR'),
            "search_close": MPath('.ww_commonImg_CloseDialog', "CSS_SELECTOR"),
            "job": MPath('memberAdd_title', 'ID'),
            # 为什么css selector不能使用value属性来定位,input[name=identity_stat][value=1] 定位失败
            "identity_common": MPath('input[name=identity_stat][checked=checked]', "CSS_SELECTOR"),
            "identity_high": MPath('input[name=identity_stat]:not([checked=checked])', "CSS_SELECTOR"),
            "extern_pos_sync": MPath('input[name=extern_position_set][checked=checked]', "CSS_SELECTOR"),
            "extern_pos_cus": MPath('input[name=extern_position_set]:not([checked=checked]', "CSS_SELECTOR"),
            "cus_input": MPath('input[name=extern_position]', "ID"),
            "send_invitation": MPath("input[name=sendInvite]", "CSS_SELECTOR"),
            "save_and_add_bottom": MPath("//form//div[3]//*[text()='保存并继续添加']"),
            "save_bottom": MPath("//form//div[3]//*[text()='保存']"),
            "cancel_bottom": MPath('//form//div[3]//*[text()="取消" and contains(@class,"js_btn_cancel")]'),
            "save_and_add_top": MPath("//form//div[3]//*[text()='保存并继续添加']"),
            "save_top": MPath("//form//div[3]//*[text()='保存']"),
            "cancel_top": MPath('//form//div[3]//*[text()="取消" and contains(@class,"js_btn_cancel")]'),
            "tips": MPath('js_tips', "ID")
        }

    def __init__(self, data={}):

        self.url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
        self.data = data

        if Common.driver:
            print("60 Contacts init里位实例化driver")
            self.driver = Common.driver
        else:
            option = webdriver.ChromeOptions()
            option.add_experimental_option('w3c', False)
            self.driver = webdriver.Chrome(options=option)
            Common().set_driver(self.driver)
            print("67 Contacts init里实例化driver")

    def open_url(self):
        pass

    def get_random_account(self):

        base_account = "Godfly"
        rand_list = list(range(10))
        rand_char = 'a b c d e f g h ij k l m n o p q r s t u v w x y z'
        rand_list += rand_char.split()
        rand_str = random.choices(rand_list, k=4)
        add_str = ''
        for item in rand_str:
            add_str += str(item)
        random_account = base_account + add_str
        return random_account

    def enter_add_member_page_by_top(self):

        self.get_locator()["add_member_top"].click()

    def input_member_base_info(self):

        # 输入用户名
        self.get_locator()["user_name"].input(self.data["username"])
        sleep(2)
        # 输入别名
        self.get_locator()["alias_name"].input(self.data["alias_name"])
        sleep(2)
        # 输入账号
        account = self.get_random_account()
        self.get_locator()["account"].input(account)

    def select_gender(self):

        if self.data['gender'] == "男":
            return
        self.get_locator()['gender_female'].click()

    def input_phone_and_email(self):

        input_list = ['phone', 'local_phone', 'email', 'address']
        for key in input_list:
            self.get_locator()[key].input(self.data[key])
            sleep(2)

    def modify_department(self):

        if self.get_locator()["department"].text == self.data['department']:
            return
        self.get_locator()["modify_depart"].click()
        sleep(2)
        self.get_locator()["search_depart"].input(self.data['department'])
        self.get_locator()['choose_depart'].click()
        sleep(2)
        self.get_locator()["search_confirm"].click()

    def input_job(self):

        self.get_locator()['job'].input(self.data['job'])
        sleep(2)

    def select_identity(self):

        if self.data["identity"] == "普通成员":
            return
        self.get_locator()['identity_high'].click()
        sleep(1)

    def select_position(self):

        if self.data["extern_position"] == "同步公司内职务":
            return
        self.get_locator()['extern_pos_cus'].click()
        sleep(1)
        self.get_locator()['cus_input'].input(self.data['cus_input'])

    def select_send_invitation(self):

        if "send_invitation" not in self.data.keys():
            return
        if self.data["send_invitation"]:
            return
        self.get_locator()["send_invitation"].click()

    def save_by_bottom(self):

        self.get_locator()["save_bottom"].click()

    def save_and_add_by_bottom(self):

        self.get_locator()["save_and_add_bottom"].click()

    def cancel_by_bottom(self):

        self.get_locator()["cancel_bottom"].click()

    def scroll_down(self):

        self.get_locator()["user_name"].scroll()

    def assert_save_success(self):

        # 也可以查数据库校验
        verity_list = [
            self.data["username"],
            self.data['phone']
        ]
        for item in verity_list:
            path = f'[title="{item}"]'
            elem_name = MPath(path, "CSS_SELECTOR")
            assert elem_name.get_element()

    def assert_save_tips_success(self):

        assert self.get_locator()["tips"].text == "保存成功"





























































