# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/17
Describe:遍历json结构转换成dict的数据类型,然后将float数据乘以times
"""
import json


def number_mod(data, times=1):
    if isinstance(data, dict):

        for k, v in data.items():
            data[k] = number_mod(v, times)
    elif isinstance(data, list):
        new_list = []
        for i in data:
            new_list.append(number_mod(i, times))
        data = new_list  # 列表嵌套列表时需要加上完成递归后的赋值
        # data = [number_mod(i, times) for i in data]

    elif isinstance(data, float):
        data = data * times
    else:
        data = data

    return data


if __name__ == "__main__":
    # temp_data = json.load(open("./quote.json", encoding="utf-8"))
    temp_data = {"a": [[1.0, 2.0, 3.0], [1.1, 2.1]]}
    print(json.dumps(number_mod(temp_data, 2), indent=2))
