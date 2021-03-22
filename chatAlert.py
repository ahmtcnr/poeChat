import shutil
import os
from os import path
import filecmp
import time
import difflib
import notify_run


import smtplib, ssl
from notify_run import Notify

from notify_run import Notify

from notify_run import Notify

notify = Notify()
val1 = input("do you want continue? y/n")

if(val1=="y"):


    while True:

        dest = shutil.copyfile("C:\Program Files (x86)\Grinding Gear Games\Path of Exile\logs\Client.txt", "C:/backupPoe/backupCopy.txt")
        print("dosya 1 kopyalandı")
        time.sleep(15)

        dest = shutil.copyfile("C:\Program Files (x86)\Grinding Gear Games\Path of Exile\logs\Client.txt", "C:/backupPoe/backupCopy1.txt")
        print("dosya 2 kopyalandı")
        file2 = open('C:/backupPoe/backupCopy.txt', 'r', encoding="utf8")
        file1 = open('C:/backupPoe/backupCopy1.txt', 'r', encoding="utf8")

        diff = difflib.ndiff(file1.readlines(), file2.readlines())
        delta = ''.join(x[2:] for x in diff if x.startswith('- '))

        if(delta!=""):
            notify.send(delta)


        file2.close()
        file1.close()


        os.remove("C:/backupPoe/backupCopy.txt")
        os.remove("C:/backupPoe/backupCopy1.txt")





