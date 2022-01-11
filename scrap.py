import requests # http requests
from bs4 import BeautifulSoup # web scraping
import smtplib # send the mail

#email body

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 

# system data and time manipluation

import datetime

now = datetime.datetime.now() # extract the current date time. email subject line 
# where it will show the appropriate date when the email was sent. 
# This shows that the same email doesn't get over written everyday. So we know that 
# everyday we are reciving an email from the automated emailer. 


#email content placeholder

content = '' # global


# extracting Hacker News Stories

def extract_news(url):
	print('Extracting Hacker News Stories...')
	cnt = ''
	cnt +=('<b>HN Top Stories:</b>\n' + '<br>' + '-'*50 +'<br>') # to make it more readable
	response = requests.get(url)  # get the content of the url and store it to reponse object
	cotent = response.content # the actually contend of the webpage use method object. 
	# scope of this content relys in the function

	soup = BeautifulSoup(content, 'html.parser')  #html parser to make thesoup.


	# From the html,parser content soup , we are interested in the components that are 
	# required. In this particular project. 

	# To understand the components, we need to look at the websites structure.

	# Object of the project. 

	# We are trying to  extract the content and autotomatically send an email to us
	# only when there is an important content for us to see, then go to website. 


	for i, tag in enumerate(soup.find_all('td', attrs={'class':'title','valign':''})):
		cnt+=((str(i+1)+' :: ' + tag.text + "\n" + '<br>') if tag.text!='More' else '')
	return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>--------<br>')
content +=('<br><br> End of Message')

#Lets send the email

# Email Authentication

print('Composing Email...')

 #update your email details

SERVER = 'smtp.gmail.com' # your smtp email server for gmail
PORT = 587 # your port number - gmail
FROM = '' # your from email id
TO = '' # your to email ids # can be a list
PASS = '' # your email id's password

msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO



msg.attach(MIMEText(content, 'html'))

print('Initiating Server...')

server = smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(1) # want to see error messages ( 1) if you don't (0)
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())

print('Email Sent...')

server.quit()