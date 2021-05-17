# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/17
Describe:
均使用mitmproxy
实现 MapLocal 修改雪球行情页的股票名称改为自己的名字
实现 Rewrite 实现股票颜色变换的的边界值测试
提交源码以及设置界面和效果的截图
"""
import json

import mitmproxy
from mitmproxy import http


class MockMitmProxyWork:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json" in flow.request.url and \
                "x=" in flow.request.url:
            # print("雪球"*10)
            print(flow)
            with open("../datas/quote.json", encoding="utf-8") as f:
                flow.response = http.HTTPResponse.make(
                    200,
                    f.read()
                )
        print("request done")

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        # 匹配规则
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json" in flow.request.url and \
                "x=" in flow.request.url:
            # 修改股票名称
            data = json.loads(flow.response.text)
            # print(data)
            # data["data"]["items"][0]["quote"]["name"] = "shimshining林"
            # data["data"]["items"][1]["quote"]["name"] = "shimshining02"
            # data["data"]["items"][2]["quote"]["name"] = "shimshining03"
            # data["data"]["items"][3]["quote"]["name"] = "shimshining04"
            # 修改涨跌幅
            data["data"]["items"][0]["quote"]["percent"] = "0.01"
            data["data"]["items"][1]["quote"]["percent"] = "-0.01"
            data["data"]["items"][2]["quote"]["percent"] = "0"
            # print(data)
            # 浮点数加倍
            data = self.number_mod(data, 2)
            flow.response.text = json.dumps(data)

    def number_mod(self, data, times=1):

        if isinstance(data, dict):

            for k, v in data.items():
                data[k] = self.number_mod(v, times)
        elif isinstance(data, list):
            # new_list = []
            # for i in data:
            #     new_list.append(number_mod(i, times))
            # data = new_list # 如果有列表嵌套列表
            data = [self.number_mod(i, times) for i in data]

        elif isinstance(data, float):
            data = data * times
        else:
            data = data

        return data


addons = [
    MockMitmProxyWork()
]

if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump

    # 使用带-s的debug模式运行
    # curl 模拟请求带参数--ssl-no-revoke
    mitmdump(["-p", "8080", "-s", __file__])


