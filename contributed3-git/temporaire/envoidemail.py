# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:14:13 2020

@author: max2b
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "poivrelerobot@gmail.com"
toaddr = "zowi.valvekens@student.umons.ac.be"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Photo prise par le robot Pepper"

body = "Normalement ça marche"

msg.attach(MIMEText(body, 'plain'))

filename = "0_Ciseau.png"
attachment = open("C:/Users/max2b/Videos/pourtest2/test/1_Ciseau.png", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "MrPepper")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()