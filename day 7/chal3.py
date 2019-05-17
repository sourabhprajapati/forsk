# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:57:15 2019

@author: SOURABH
"""
import requests
url1 = "http://free.currencyconverterapi.com/api/v5/convert"
url2 = "?q=USD_INR&compact=y"
url3 = "&apiKey=adabfa70182ee963f7ba"
url = url1 + url2 + url3
print (url)


response = requests.get(url)