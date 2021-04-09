#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:
Describe:
"""

import allure
import pytest


def test_attach_text():
    allure.attach("这是attach文本测试",
                  attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>HTML body 区域</body>",name="HTML测试",
                  attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file("D:/personProc/hogwarts_shining/resource/1.png",
                  name="图片1", attachment_type=allure.attachment_type.PNG)


def test_attach_video():
    allure.attach.file("D:/personProc/hogwarts_shining/resource/xxx.video",
                  name="视频A",attachment_type=allure.attachment_type.MP4)

if __name__ == "__main__":
    pytest.main()