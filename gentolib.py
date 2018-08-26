import get_libgen_data
import mail
import requests
import html5lib
import sys
import html5lib
from bs4 import BeautifulSoup
from tabulate import tabulate
import pydoc


search_term = ' '.join(sys.argv[1:])
libgen_url = "http://libgen.io/search.php?req=" + search_term

r = requests.get(libgen_url)
libgen_soup = BeautifulSoup(r.content, "html5lib")

#Dictionary data from Libgen based on search
libgen_data = get_libgen_data.get_libgen_data(libgen_soup)

print "\n"
for x in libgen_data:
	author = libgen_data[x]["author"]
	title = libgen_data[x]["title"]
	extension = libgen_data[x]["extension"]
	num_pages = libgen_data[x]["num_pages"]
	year_published = libgen_data[x]["year_published"]
	extension = libgen_data[x]["extension"]
	size = libgen_data[x]["size"]

	print "[%d] %s - %s [%s pages (%s)] - %s %s \n" % (x, title, author, num_pages, year_published, size, extension) + "\n"

print "Please enter the index of the book you want"
selection = int(raw_input("Index > "))

print "\nDownloading book..."

request_book = requests.get(get_libgen_data.get_download_url(libgen_data[selection]["download_link"]), stream=True)


print "Saving Book..."
book_name = libgen_data[selection]["title"] + "." + libgen_data[selection]["extension"]
path = "./" + book_name

with open(book_name, 'wb') as handle:
    for block in request_book.iter_content(4096):
        handle.write(block)


print "Sending Book to your Kindle..."

mail.send_to_kindle(book_name, path)

print "Book sent to your kindle ! Enjoy"

