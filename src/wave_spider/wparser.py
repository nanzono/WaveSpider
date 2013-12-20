# coding:utf-8

from bs4 import BeautifulSoup

import os
import codecs

class WParser(object):

    def __init__(self):
        self.store_path = r"../../store"

    def parse(self):
        for root, dirs, files in os.walk(self.store_path):
            for file in files:
                file_no, ext = os.path.splitext(file)
                if ext != ".html":
                    continue
                file_path = os.path.join(self.store_path, file)
                page = WavePage(file_path)
                page.parse()



class WavePage(object):

    def __init__(self, file_path):
        self.file_path = file_path
        fi = codecs.open(file_path, "r", "utf-8")
        self.soup = BeautifulSoup(fi)

    def parse(self):

        questions = self.soup.findAll("div", {"class":"ok_resultlist"})

        parsed_result = list()

        for q in questions:
            qp = {}
            qp["title"] = q.find("p", {"class": "qat"}).text
            qp["detail"] = q.find("p", {"class": "q_datail"}).text
            parsed_result.append(qp)

        h2_title = self.soup.find("h2").text

        print h2_title
        for p in parsed_result:
            print u"[質問]"
            print p["title"]
            print u"[本文]"
            print p["detail"]
            print ""
        print ""







def main():
    wp = WParser()
    wp.parse()


if __name__ == '__main__':
    main()
