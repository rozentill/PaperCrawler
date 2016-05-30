#! /usr/env/bin
#-*-coding:utf8-*-

import re
import requests
import datetime
from bs4 import BeautifulSoup
from parser import parser

s = requests.session()
basic_url = 'https://ideas.repec.org'

def conference_parse(url,result):
    resp = s.get(url)
    print 'Get the conference/journal page.'
    soup = BeautifulSoup(resp.content, 'html.parser')
    paperlist = soup.find_all('ul',{'class':'paperlist'})
    for pl in paperlist:

        li = pl.find_all('li')

        for paper in li:

            paper_url = paper.b.a.get('href')
            print 'A new paper captured.'
            # return basic_url+paper_url
            soup_paper = BeautifulSoup(s.get(basic_url+paper_url).content,'html.parser')

            result.append(parser(soup_paper,basic_url+paper_url))

            print 'A new paper crawled successfully.'

    print 'One conference or journal finished.'


if __name__ == '__main__':


    print 'Start to crawl the website...'

    html = s.get('https://ideas.repec.org/i/pall.html')
    soup = BeautifulSoup(html.content, 'html.parser')

    print 'Get the index page.'

    trow = soup.find_all('tr')

    result = []

    with open ('result.txt','w') as f:

        print 'The result file now is open.'

        for tr in trow:
            if len(tr.find_all('td')) is 4:
                print 'Find a conference or journal.'
                conference_url = basic_url + tr.find_all('td')[2].a.get('href')
                conference_parse(conference_url,result)

                if len(result) > 1000:
                    for r in result:
                        f.write(str(r)+'\n')
                    result = []
