#!/usr/bin/python
# Put this code into a file named "pifinder.py" in /home/pi/

# This script finds the IP address of the RPi and sends it to you in an email when using headless configuration.

import smtplib, string, subprocess
################################### EDIT HERE ###################################
#
# Replace the * here with your Mines username to complete the email address
minesEmail = "bbernstein@mymail.mines.edu"
#
# This is NOT your MultiPass password. Go to identity.mines.edu to get your IMAP/IMOP password and paste it here
imapPassword = "^mRk8Ik%ry*LKYSD"
#
################################### EDIT HERE ###################################

# Get the output of ifconfig
if_config = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]

# Form the body of the email
body = string.join((
        "From: %s" % minesEmail,
        "To: %s" % minesEmail,
        "Subject: RPi IP Address",
		"",
        "Find the section below starting with 'wlan#', then take the number after 'inet' from the next line. That is the IP address of your RPi!",
		"",
		if_config,
        ), "\r\n")

# Send the email  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(minesEmail, imapPassword)  
server.sendmail(minesEmail, minesEmail, body)  
server.quit()
