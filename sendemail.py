import smtplib 
from_addr = '' 
from_name=''
msg="I want to have your gieko car insurance plan"
to_name="Brittany Blake"
subject="This is my confession"
to_addr  = '' 
message = """From: {} <{}> 
To: {} <{}> 
Subject: {} 
{} 
""" 
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg) 
# Credentials (if needed) 
username = '' 
password = '' 
# The actual mail send 
server = smtplib.SMTP('smtp.gmail.com:587') 
server.starttls() 
server.login(username, password) 
server.sendmail(from_addr, to_addr, message_to_send) 
server.quit() 
