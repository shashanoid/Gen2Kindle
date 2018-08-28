# Purpose of this file is to upload the downloaded book to your kindle via email
# Please Read the three comments mentioned below and fill those blanks to set up uploading to kindle
# 


import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

#The email which your kindle is registered with -- Approved Personal Document E-mail List 
fromaddr = ""

#Your kindle email [@kindle.com] - Find under [Send-to-Kindle E-Mail Settings]
toaddr = ""
 


def send_to_kindle(subject, path, file_name):
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = subject

	body = ""

	msg.attach(MIMEText(body, 'plain'))
 
	if file_name != None:
		filename = file_name + '.pdf'
	else:
		filename = subject

	attachment = open(path, "rb")
 
	part = MIMEBase('application/x-mobipocket-ebook', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
	msg.attach(part)
 
 	### IMPORTANT ###
 	# Microsoft Live = smtp.live.com, For gmail use smtp.gmail.com and so on..

	server = smtplib.SMTP('smtp.live.com', 587)
	server.starttls()

	#Password of the email your kindle is registed with
	server.login(fromaddr, "")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
