html_doc = """
<html><head><title>The Dormouse story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
import requests

chelsea_info = requests.get('https://en.wikipedia.org/wiki/Chelsea_F.C.')
soup1 = BeautifulSoup(html_doc, 'lxml')
soup2 = BeautifulSoup(chelsea_info.content, 'lxml')
soup3 = BeautifulSoup('<b class = "boldest">Extremely bold</b>', 'lxml')
#soup4 = BeautifulSoup('<p class="body strikeout"></p>')

#print(soup.prettify())
'''print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id="link3"))'''

for link in soup2.find_all('a'):
    print(link.get('href'))

#print(soup2.get_text())

'''tag = soup3.b
print(tag)
print(type(tag))
print(tag.name)
print(tag['class'])
print(tag.attrs)
tag['class'] = 'verybold'
tag['id'] = 1
print(tag)
del tag['class']
print(tag)
del tag['id']
print(tag)
print(tag.get('class'))'''
