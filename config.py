#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author by pekingzcc -*-
# -*- date : 2017-05-19 -*-

"""配置文件
"""

# 采集的站点
PROXY_SITES = [

    'http://www.rmccurdy.com/scripts/proxy/good.txt',

]

# 代理输出位置
OUTPUT_FILE = "proxy_list.txt"


# User-Agent list
USER_AGENT_LIST = [
    'Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
    'Microsoft Internet Explorer/4.0b1 (Windows 95)',
    'Opera/8.00 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
    'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
]


# 超时时间
TIME_OUT = 4

#重试次数
RETRY_NUM = 3

# 代理正则
PROXY_REGX = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,4}"

# 测试URL
TEST_URL = "http://www.baidu.com"