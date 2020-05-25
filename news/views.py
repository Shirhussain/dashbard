from django.shortcuts import render

import requests
requests.packages.urllib3.disable_warnings()


from bs4 import BeautifulSoup

def scrape():
	session = requests.Session()
	session.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
	url = "https://www.bbc.com/news/business"

	content =session.get(url, verify=False).content
	soup = BeautifulSoup(content, "html.parser")

	columns = soup.find_all('div',{'gel-layout gel-layout--equal'})
	print(len(columns))

scrape()
