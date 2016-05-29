#! /usr/env/bin
#-*-coding:utf8-*-

import re
import requests
import datetime
from bs4 import BeautifulSoup
from parser import parser

def conference_parse(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    paperlist = soup.find_all('ul',{'class':'paperlist'})
    for pl in paperlist:
        li = pl.find_all('li')
        for paper in li:
        paper_url = paper.b.a.get('href')
            return basic_url+paper_url
            # return parser(basic_url+paper_url)


if __name__ == '__main__':

    s = requests.session()

    html = requests.get('https://ideas.repec.org/i/pall.html')
    soup = BeautifulSoup(html.content, 'html.parser')

    trow = soup.find_all('tr')

    with open ('url_list.txt') as f:
        for tr in trow:
            if len(tr.find_all('td')) is 4:
                conference_url = basic_url + tr.find_all('td')[2].a.get('href')
                f.write(conference_parse(conference_url))
