# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/18
Describe:
"""
import requests
from jsonpath import jsonpath
from hamcrest import *
from requests.auth import HTTPBasicAuth


class TestHTTPGet:

    def test_http_get(self):
        url = "https://httpbin.testing-studio.com/get"
        r = requests.get(url)
        print(r.text)
        print(r.json())
        print(r.status_code)
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "shining"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post(self):
        payload = {
            "level": 1,
            'name': "shining"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_headers(self):
        headers = {'user-agent': "shimshining"}
        r = requests.get("https://httpbin.testing-studio.com/get", headers=headers)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['headers']["User-Agent"] == "shimshining"

    def test_post_json(self):
        payload = {
            "level": 1,
            'name': "shining"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["json"]["level"] == 1

    def test_get_json_assert(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        r.status_code == 200
        assert r.json()["category_list"]["categories"][0]["name"] == "开源项目"
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == "开源项目"

    def test_hamcrest_assert(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        r.status_code == 200
        assert r.json()["category_list"]["categories"][0]["name"] == "开源项目"
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == "开源项目"
        assert_that(jsonpath(r.json(), '$..name')[0], equal_to("开源项目"))

    def test_headers_cookie(self):
        url = "https://httpbin.testing-studio.com/cookies"
        headers = {"Cookie": 'working=1', 'User-Agent': 'python-requests/2.23'}
        r = requests.get(url, headers=headers)
        print(r.request.headers)

    def test_cookies(self):

        url = "https://httpbin.testing-studio.com/cookies"
        headers = {'User-Agent': 'python-requests/2.23'}
        cookies = dict(cookies_are="shimshining")
        r = requests.get(url, headers=headers, cookies=cookies)
        print(r.request.headers)

    def test_auth(self):

        url = "https://httpbin.testing-studio.com/basic-auth/shining/123"
        r = requests.get(url, auth=HTTPBasicAuth("shining", "123"))
        print(r.status_code)
        print(r.json())
        assert_that(r.status_code, equal_to(200))

