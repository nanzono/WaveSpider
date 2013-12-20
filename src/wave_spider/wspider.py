# coding:utf-8


import urllib2
import urllib
import os
import time


class WSpider(object):


    def __init__(self, keyword, crawl_page_cnt):
        self.keyword = keyword
        self.crawl_page_cnt = crawl_page_cnt

        self.store_path = r"../../store"

    def create_query(self, keyword, page_no):

        keyword = urllib.quote(keyword.encode("utf-8"))
        temp_url = u'http://okwave.jp/searchkeyword/%(keyword)s/%(page_no)d/'
        crawl_url = temp_url % { 'keyword': keyword, 'page_no': page_no}
        return crawl_url

    def crawl_store(self, crawl_url, page_no):

        page = urllib2.urlopen(crawl_url)

        file_name_list = {}
        file_name_list["keyword"] = self.keyword
        file_name_list["page_no"] = '%(#)08d'%{'#':page_no}

        file_name = "%(keyword)s_%(page_no)s.html" % file_name_list
        file_path = os.path.join(self.store_path, file_name)

        fo = open(file_path, "wb")
        fo.write(page.read())
        fo.close()

    def get_page(self):

        for i in range(self.crawl_page_cnt):
            crawl_url = self.create_query( self.keyword, i+1)
            self.crawl_store(crawl_url, i+1)
            time.sleep(1)


def main():
    ws = WSpider( u"ビール", 10)
    ws.get_page()


if __name__ == '__main__':
    main()


