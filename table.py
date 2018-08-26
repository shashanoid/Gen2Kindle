import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "shashwat@greenlie.org"
toaddr = "shashwat_85@kindle.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE EMAIL"
 
body = ""
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "Anything.pdf"
attachment = open("/Users/shashwatsingh/Desktop/GenToKindle/Facebook.pdf", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.live.com', 587)
server.starttls()
server.login(fromaddr, "")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
