#!/usr/bin/env python3
#-*- coding=utf-8 -*-

from scrapy.cmdline import execute
def main():
    execute(['scrapy', 'crawl', 'novelSpider'])

if __name__ == "__main__":
    main()
    pass
