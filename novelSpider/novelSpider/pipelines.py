# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NovelspiderPipeline(object):
    def process_item(self, item, spider):
        # print(item['novelChaper'])
        # print(item['novelContent'])
        with open(item['bookName']+'.csv','a') as mBook:
            mBook.write('------------------------------------------------------------------'+'\n')
            mBook.write(str(item['novelIndex'])+',')
            mBook.write(item['novelChaper']+'  ')
            # mBook.write('\n')
            mBook.write(item['novelContent'])
            mBook.flush()
        return item

