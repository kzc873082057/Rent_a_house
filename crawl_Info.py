#_*_coding:utf-8_*
from bs4 import BeautifulSoup
from urllib import parse
import csv
#location = 地方，price = min_max
base_url = "http://zh.58.com/{location}/chuzu/pn{page}/?minprice={price}"

url = base_url.format(location="zhgxq",page ="0",price="0_5000")



