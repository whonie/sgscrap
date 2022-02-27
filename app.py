from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
from bs4 import BeautifulSoup
client = MongoClient('localhost', 27017)
db = client.dbtest

























# import requests
# import ssl
# from requests_html import HTMLSession
# from requests_html import AsyncHTMLSession
# import urllib.request
# from urllib.request import urlopen
#
# # ssl._create_default_https_context = ssl._create_unverified_context
#
#
# # naverUrl ='https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303'
# # naverMovies = '#old_content > table > tbody > tr'
# schoolUrl = 'https://sogang.ac.kr/bachelor/students/notice/notice08.html'
# schoolMenus = '#body > div.aside > ul > li.on > ul > li'
#
#
# response = urllib.request.urlopen(schoolUrl)
# print(response.read().decode("utf-8"))
#
#
#
#
# # data = soup.select('h4.card-text')
#
#
#
#
# # headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
# # data = requests.get(schoolUrl ,headers=headers, verify=False)
# # soup = BeautifulSoup(data.text, 'html.parser')
# # menus = soup.select(schoolMenus)
# #
# # r = urllib.request.urlopen(schoolUrl)
#
#
#
#
#
#
#
#
# #body > div.aside > ul > li.on > ul > li:nth-child(1)

