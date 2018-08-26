import requests
import html5lib
import sys
import html5lib
from bs4 import BeautifulSoup


def get_libgen_data(soup):
	body = soup.find_all('tbody')
	one = body[2]
	counter = len(one.find_all('tr'))
	data = {}

	for each_row in xrange(1, counter):
		row = one.find_all('tr')[each_row]
		author = row.find_all('td')[1].text
		title = row.find_all('td')[2].text.split(":")[0]
		publisher = row.find_all('td')[3].text
		year_published = row.find_all('td')[4].text
		num_pages = row.find_all('td')[5].text
		size = row.find_all('td')[7].text
		extension = row.find_all('td')[8].text
		download_link = row.find_all('td')[10].a["href"]

		data.update({each_row: {'author': author, 'title':title, 'publisher':publisher, 'year_published':year_published, 
					'num_pages':num_pages, 'extension': extension, 'download_link': download_link, 'size': size}})

		
	return data


def get_download_url(link):
	r = requests.get(link)
	download_soup = BeautifulSoup(r.content, "html5lib")
	download_link = str(download_soup.find_all('a')[1]["href"])
	return download_link
