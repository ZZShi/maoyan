# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class MaoyanItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movieName = Field()     # 电影名称
    movieId = Field()       # 电影ID
    approve = Field()       # 评论赞成数
    cityName = Field()      # 城市名
    content = Field()       # 评论正文
    score = Field()         # 评分
    userId = Field()        # 用户ID
