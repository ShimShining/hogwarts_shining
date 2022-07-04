# -*- coding: utf-8 -*-
"""
Author : 'Shining'
Date: 2021/5/21
Describe:
"""
import json

import jsonpath


def get_tag_id_by_dict(name, group_name):

    with open("./wework.json", encoding="utf-8") as f:
        data = json.loads(f.read(), encoding="utf-8")
        groups = data["tag_group"]
        for group in groups:
            if group["group_name"] == group_name:
                for tag in group["tag"]:
                    if tag["name"] == name:
                        return tag["id"]
                else:
                    return None
        else:
            return None


def get_tag_id(name, group_name):

    demo = {
  "errcode": 0,
  "errmsg": "ok",
  "tag_group": [
    {
      "group_id": "etkb_0EAAALSeacRGKUY1Vfx_P-8mHXA",
      "group_name": "客户等级",
      "create_time": 1621581550,
      "tag": [
        {
          "id": "etkb_0EAAADJP3wbC4NtIKIvC6J3NPkA",
          "name": "一般",
          "create_time": 1621581550,
          "order": 0
        },
        {
          "id": "etkb_0EAAAeVrPsgrDsnCcPeH4R3p21Q",
          "name": "重要",
          "create_time": 1621581550,
          "order": 0
        },
        {
          "id": "etkb_0EAAARWGbYnYAHNGbUCRdljh8Jw",
          "name": "核心",
          "create_time": 1621581550,
          "order": 0
        }
      ],
      "order": 0
    },
    {
      "group_id": "etkb_0EAAAerkitVlzCEKEdiFx5CvpXQ",
      "group_name": "demo",
      "create_time": 1621581996,
      "tag": [
        {
          "id": "etkb_0EAAAkdxC4A6P37JwohlZnXRPNQ",
          "name": "demo_tag1",
          "create_time": 1621581996,
          "order": 0
        }
        ],
      "order": 0
            }
        ]
    }
    val = '$..tag_group..tag[?(@.name=="一般")]'
    val2 = '$..*[?(@.group_name=="demo")].tag[?(@.name=="demo_tag1")].id'
    # *[?(@.group_name="客户等级")]..*[?(@.name="一般")]
    print(jsonpath.jsonpath(demo, val2))

    fliter = '$..*'
    # [?(@.group_name="{group_name}")]..*[?(@.name="{name}")]
    print(fliter)
    with open("./wework.json", encoding="utf-8") as f:
        content = f.read()
        print(type(content))
        content = json.loads(content, encoding="utf-8")
        print(type(demo))
        print(type(content))
        print("++++++++++++++++++++")
        print(jsonpath.jsonpath(content, '$..tag_group..group_name'))
        print("+++++++++++++++++++++")
        # print(tag_ids)
        # return tag_ids
        # tag_id = tag_ids[tag_ids.index(name)-1]
        # return tag_id

if __name__ == "__main__":
    # res_id = get_tag_id_by_dict("demo_tag1", "demo")
    # print(res_id)
    res_id = get_tag_id("demo_tag1", "demo")
    print(res_id)