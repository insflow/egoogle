# -*- coding: utf-8 -*-
import requests
from lxml import etree
import re
import json


def get_google_result(key):
    data = {"newwindow":"1", "hl":"zh-CN", "site":"webhp","q":key,"btnG":"Google 搜索","oq":key,"gs_l":"serp.12..0l10.532197.536226.0.549811.1.1.0.0.0.0.8490.8490.9-1.1.0.ckpsrh...0...1.1j4.64.serp..0.1.8490.PJNi7qZDvmw" }
    proxies = {
         "http": "http://104.131.134.166:3128"
    }

    r = requests.get("https://www.google.com.hk/search", params=data, timeout=1)
    page = etree.HTML(r.text)
    result = page.xpath("/html/body/script[3]/text()")
    patt = re.compile(r"\((.*?)\)", re.I | re.X)
    m = patt.findall(result[0])
    d = json.loads(m[0])
    result_data = ""
    for str in d['rfs']:
        result_data = result_data + str + ":"
    return result_data[:-1]
#print get_google_result('belt')
