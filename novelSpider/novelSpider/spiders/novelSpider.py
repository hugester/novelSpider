#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
# from bs4 import BeautifulSoup
from novelSpider.items import NovelspiderItem

class NovelSpiderSpider(scrapy.Spider):
    name = "novelSpider"
    allowed_domains = ["zwdu.com"]
    start_urls = ["https://www.zwdu.com/book/34287/"]
    bookName = None
    # root_url = "https://www.zwdu.com/book/7611/"
    # start_urls = ["https://www.zwdu.com/book/7611/12213775.html"]
    
    def parse(self,response):
        # mNover = NovelspiderItem()
        # mNover['novelUrlList'] = None
        # mNover['name'] = None
        # mNover['author'] = None

        # print(response.text)
        # if response.xpath("//div[@id='info']/h1").extract()[0] == "黑暗血时代":
        # print(response.xpath("//dd/a/@href").extract())
            
        novelUrlList = response.xpath("//dd/a/@href").extract()
        # chapterCount = str(len(novelUrlList))
        self.bookName = response.xpath('//div[@id="info"]/h1/text()').extract()[0]
        author = response.xpath('//div[@id="info"]/p/text()')[0].extract().split("：")[-1]
        with open(self.bookName+'.csv','w') as mBook:
            mBook.write('0,'+self.bookName+',作者,')
            mBook.write(author+'\n')
            # mBook.write(chapterCount+'\n')
            mBook.flush()
        a = 0
        b = 3
        # if mNover['novelUrlList']:
        # print("################################################")
        for index,urls in enumerate(novelUrlList,1):              
            postUrl = self.start_urls[0] + urls.split('/')[-1]
            chapterIndex = index
            # print(postUrl)
            # print(postUrl)
            if a <b:
                yield Request(url=postUrl,callback=self.pareChapterPage,meta={"index":chapterIndex,"bookName":self.bookName})
                a += 1
            pass

    def pareChapterPage(self,response):
        mNover = NovelspiderItem()
        mNover['bookName'] = response.meta['bookName']
        mNover['novelIndex'] = response.meta['index']
        mNover['novelChaper'] = response.xpath('//div[@class="bookname"]/h1/text()').extract()[0]
        chaperContent = response.xpath('//div[@id="content"]/text()').extract()
        mChapterContent=[]
        for mContent in chaperContent:
            mChapterContent.append("".join(mContent.split()))
        mNover['novelContent']=''.join(str(e) for e in mChapterContent)
        yield mNover
        pass
        

