import requests	
from bs4 import BeautifulSoup

base_url = 'https://www.nytimes.com/'
r = requests.get(base_url)
r_html = r.text

soup = BeautifulSoup(r_html,'html.parser')
title = soup.title

#print(soup.prettify())
#print(soup.find_all(class_="css-8uvv5f esl82me2"))
#print(soup.find_all(class_="css-78b01r esl82me2"))

list=soup.find_all(class_="esl82me2")

for i in list:
 print(i.text)
