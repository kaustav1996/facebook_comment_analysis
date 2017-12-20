import os
import urlparse
import urllib
import csv
from bs4 import BeautifulSoup
import time
from selenium import webdriver
url="https://www.facebook.com/bitcoinchart/posts/1673316632734559"
browser = webdriver.PhantomJS(executable_path='./phantomjs')
browser.get(url)
time.sleep(5)
htmltext = browser.page_source
report=[0,0,0]
total=0
soup= BeautifulSoup(htmltext,"lxml")
post=soup.find('div',{'class':'_5pcr userContentWrapper'})
print (post.text.decode("ascii"))
for comments in post:
	print(comments.text)
print(2)