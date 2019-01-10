# -*- coding: utf-8 -*-
import json
import time
import scrapy
from scrapy.http import Request

"""

快妖精App的视频以及视频信息抓取
"""

class Kyj344SpiderItem(scrapy.Item):
    #视频id
    id = scrapy.Field()
    #标题
    title = scrapy.Field()
    #封面
    thumb = scrapy.Field()
    #视频
    video = scrapy.Field()
    #喜欢
    likes = scrapy.Field()
    #观看
    views =  scrapy.Field()
    #添加时间
    addtime = scrapy.Field()
    #用户
    user = scrapy.Field()
    #file_paths
    file_paths = scrapy.Field()
class Kyj344Spider(scrapy.Spider):
    name = 'kyj344'
    allowed_domains = ['kyj344.com',"kuaiyaojing.info"]
    def start_requests(self):
        for p in range(1,101528):
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
            }
            url = "http://app.kyj344.com:8880/api/public/?service=Video.getVideo&uid=-1&videoid={}".format(p)
            yield Request(url=url,headers=headers)

    def parse(self, response):
        content = response.body_as_unicode()
        if content:
            ret = json.loads(content)
            data = ret.get("data")
            code = data.get("code")

            if code == 0:
                info = data.get("info")[0]

                is_ad = info.get("is_ad")

                if is_ad == "0":
                    item = Kyj344SpiderItem()

                    item["id"] = info.get("id")
                    item["title"] = info.get("title")
                    item["thumb"] = info.get("thumb")
                    item["video"] = info.get("href")
                    item["likes"] = info.get("likes")
                    item["views"] = info.get("views")
                    item["addtime"] = info.get("datetime")
                    user = {}

                    userinfo = info.get("userinfo")
                    user["name"] = userinfo.get("user_nicename")
                    user["userId"]= userinfo.get("id")
                    user["city"] = userinfo.get("city")
                    user["age"] = userinfo.get("age")
                    user["avatar_thumb"] = userinfo.get("avatar_thumb")
                    user["fans"] = userinfo.get("fans")
                    user["follows"] = userinfo.get("follows")
                    user["workVideos"] = userinfo.get("workVideos")
                    user["likeVideos"] = userinfo.get("likeVideos")
                    user["gender"] = "male" if userinfo.get("sex",1) else "female"
                    item["user"] = user

                    yield item


