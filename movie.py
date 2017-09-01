# coding=utf-8
import random
import string

import requests
import time
from bs4 import BeautifulSoup


class movie(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/subject/26363254/comments?start=0&limit=20&sort=new_score&status=P'
        self.comments = set()
        self.headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;",
                   "Accept-Encoding": "gzip",
                   "Accept-Language": "zh-CN,zh;q=0.8",
                   "Referer": "https://movie.douban.com/",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}
        self.bid = "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))
        self.cookies=''+self.bid+'; ll="108288"; ps=y; _vwo_uuid_v2=8415D10997C5F1ED92AC402D470F1DD8|431f8135fd0af3f3bdaff6e680994d00; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1504086135%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DMabkIODNm2UeCLlAe4hg3JWkgj24Q1mPKrj2lpClqsHNqhr8w8Kp9GlUlrt9Yq_w%26wd%3D%26eqid%3D98e9ebba00007f2d0000000359a67656%22%5D; __utmt=1; dbcl2="120639193:Iv/iu3Ncz9k"; ck=s_NB; __utma=30149280.1967324195.1483428856.1504081487.1504086135.15; __utmb=30149280.12.10.1504086135; __utmc=30149280; __utmz=30149280.1504081487.14.13.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.12063; __utma=223695111.1201897251.1495417534.1504081487.1504086164.3; __utmb=223695111.0.10.1504086164; __utmc=223695111; __utmz=223695111.1504081487.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=12fe56d53fe0d9d9.1495417534.3.1504087522.1504082847.; _pk_ses.100001.4cf6=*; ap=1'
    def _toto_cookies(self):
        cookies = {}
        for line in self.cookies.split(';'):
            key, value = line.split('=', 1)
            cookies[key] = value
        return cookies

    def main(self):
        page = 188519/20
        count = 0
        for i in range(0,page):
            url = 'https://movie.douban.com/subject/26363254/comments?start=%s&limit=20&sort=new_score&status=P' %count
            print url
            count += 26
            content = requests.get(url, headers=self.headers,cookies=self._toto_cookies())
            if(content.status_code != 200):
                exit('页面异常,退出')
            soup = BeautifulSoup(content.text, 'html.parser')
            comment_list = soup.find_all('div', class_='comment')
            self._toto_comment(comment_list)
            if(i % 5 == 0):
                print '休息2秒'
                time.sleep(2)
            if(i==page):
                break
        print len(self.comments)
    def _toto_comment(self,comment_list):
        for comment in comment_list:
            # print comment.find('p').get_text()
            self.comments.add(comment.find('p').get_text())


if __name__ == '__main__':
    movie().main()