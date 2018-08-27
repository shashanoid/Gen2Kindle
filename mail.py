import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

#Your email which is registred in Kindle
fromaddr = ""

#Your kindle email
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
 
	server = smtplib.SMTP('smtp.live.com', 587)
	server.starttls()
	#Your password of the kindle email you registered with
	server.login(fromaddr, "")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
