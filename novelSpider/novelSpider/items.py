# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelspiderItem(scrapy.Item):
    # define the fields for your item here like:
    novelChaper = scrapy.Field() #小说章节
    novelContent = scrapy.Field() #小说内容
    novelIndex = scrapy.Field() #章节编号
    bookName = scrapy.Field()

    pass
