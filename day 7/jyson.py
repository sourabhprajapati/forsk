# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:30:26 2019

@author: SOURABH
"""

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=b22b7a71152a49b65fe1ddafc5294b5a"

url = url1 + url2 + url3
print (url)


response = requests.get(url)