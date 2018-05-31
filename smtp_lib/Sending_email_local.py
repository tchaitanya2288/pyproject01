#!/usr/bin/python

import smtplib

sender = 'tchaitanya.2288@gmail.com'
receiver = ['t.chaitanya8822@gmail.com']

message = """From: From Person <tchaitanya.2288@gmail.com>
To: To Person <t.chaitanya8822@gmail.com>
Subject: SMTP e-mail test
This is a test e-mail message."""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")