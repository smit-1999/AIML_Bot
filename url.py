import urllib2
from bs4 import BeautifulSoup

# response = urllib2.urlopen('https://www.ubuntupit.com/top-20-highest-paying-computer-science-jobs/')
# html = response.read()
# soup = BeautifulSoup(html)
# lis = []
# for tag in soup.find_all(class_="ftwp-heading") :
  
# 	print(tag.attrs)
#print(html)
def topTrending():
	response = urllib2.urlopen('https://www.upgrad.com/blog/top-10-highest-paying-jobs-in-india/')
	html = response.read()
	#print(html)
	soup = BeautifulSoup(html, 'html.parser')
	jobs = []
	for title in soup.find_all(class_="ez-toc-list") :	
		items = [item.text.encode("utf-8") for item in title.select('li')]
		#print(items)
		jobs = items
	return jobs
# jobs = topTrending()
# print(type(jobs))
