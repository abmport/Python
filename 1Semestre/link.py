from BeautifulSoup import BeautifulSoup
import urllib2
import re
#IDEA DEVELOPERS
#@ideadevelopers

def getLinks(url):
html_page = urlib2.urlopen(url)
soup = BeautifulSoup(html_page)
links = []
for link in soup.findAll('a',attrs={'href': re.compile("^http:\\")}): links.append(link.get('href'))
return links
links = getLinks("http://www.teacheidea.com")
print (links)
