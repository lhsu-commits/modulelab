#!/usr/bin/env python3

import email.message
import os
import psutil
import re
import smtplib
import socket

while True:
    message = email.message.EmailMessage()
    message["From"] = "automation@example.com"
    message["To"] = "{}@example.com".format(os.environ.get('USER'))
    message.set_content("Please check your system and resolve the issue as soon as possible.")
    #check CPU utilization > 80% in use
    if (psutil.cpu_percent(interval=1) > 80):
        message["Subject"] = "Error - CPU usage is over 80%"
        mail_server = smtplib.SMTP('localhost')
        mail_server.send_message(message)
        mail_server.quit()
    #check disk utilization < 20% available
    tmp_disk_metric = str(psutil.disk_usage('/')).split("=")
    tmp_disk_usage = str(tmp_disk_metric[4])
    disk_usage = tmp_disk_usage[0:len(tmp_disk_usage)-1]
    if (float(disk_usage) < 20.0):
        message["Subject"] = "Error - Available disk space is less than 20%"
        mail_server = smtplib.SMTP("localhost")
        mail_server.send_message(message)
        mail_server.quit()
    #check memory utilization < 500 MB available
    tmp_mem_metric = str(psutil.virtual_memory()).split(",")
    tmp_available = tmp_mem_metric[1].split("=")
    mem_available = tmp_available[1]
    mem_threshold = 500 * 1024 * 1024
    if (int(mem_available) < mem_threshold):
        message["Subject"] = "Error - Available memory is less than 500MB"
        mail_server = smtplib.SMTP("localhost")
        mail_server.send_message(message)
        mail_server.quit()
    #check localhost name resolution
    if (socket.gethostbyname("localhost") != "127.0.0.1"):
        message["Subject"] = "Error - localhost cannot be resolved to 127.0.0.1"
        mail_server = smtplib.SMTP("localhost")
        mail_server.send_message(message)
        mail_server.quit()
