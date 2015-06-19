from bs4 import BeautifulSoup as bs
import urllib2
url="http://cs.uoi.gr/index.php?menu=m5"
urs="http://cs.uoi.gr/"
content = urllib2.urlopen(url).read()
soup = bs(content)
soup=soup.findAll('div', attrs={'class': 'newPaging'})
for i in range(0,7):
	print "\n"
	print soup[i].text.strip().replace("\n\r\n\t\t","\n")
	print str(urs+str(soup[i].a.get('href')))
	print "\n"
