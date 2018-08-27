#!/usr/local/bin/python
import get_libgen_data
import mail
import requests
import html5lib
import sys
import html5lib
from bs4 import BeautifulSoup
import os
import subprocess


def main():
	search_term = ' '.join(sys.argv[1:])
	if not search_term:
		print "Please provide a search term"
	else:
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
		
		print "Please enter the index of the book you want or press any other key to search again"
		selection = int(raw_input("Index > "))
		
		print "\nDownloading book..."
		
		request_book = requests.get(get_libgen_data.get_download_url(libgen_data[selection]["download_link"]), stream=True)
		
		
		print "Saving Book..."
		book_name = libgen_data[selection]["title"] + "." + libgen_data[selection]["extension"]
		path = "./" + book_name
		output_name = libgen_data[selection]["title"] + ".mobi"
		
		output_path = "./" + output_name
		
		with open(book_name, 'wb') as handle:
		    for block in request_book.iter_content(4096):
		        handle.write(block)
		
		send_mail = raw_input("Do you wish to send it to your kindle? (y/n) :> ")
		
		#downloaded file extension
		extension = os.path.splitext(book_name)[1]
		
		def convert_and_send_mobi():
			print "Converting to mobi"
			cmd = './kindlegen'
			process = subprocess.Popen([cmd, path])
			process.wait()
			mail.send_to_kindle(output_name, output_path, None)
			print "File sent to kindle, please give it some time to appear"
		
		if send_mail == "y":
			if extension == '.pdf':
				mail.send_to_kindle('Convert', path, libgen_data[selection]["title"])
				print "PDF converted and sent to your kindle, please give it some time to appear since its converted on amazon's end."
			elif extension == '.epub':
				convert_and_send_mobi()
			else:
				mail.send_to_kindle(book_name, output_path, None)
				print "Sent to your kindle, please give it some time to appear"
		else:
			print "Book saved."

		search_again = raw_input("Enter 'exit' or search again: ")

		if search_again != "exit":
			main()
		else:
			return None



if __name__ == '__main__':
    main()
