from django.shortcuts import render
from .models import *

# Create your views here.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def index(request):
    profile = Profile.objects.all()[0]
    ipaddress = request.META['REMOTE_ADDR']
    print(ipaddress)
    logs = AccessLog.objects.filter(ipaddress=ipaddress)
    if logs:
        log = logs[0]
        log.count += 1
        log.save()
    else:
        log = AccessLog()
        log.ipaddress = ipaddress
        log.count = 1
        log.save()
    if request.method == "POST":
        mail = MyMail()
        mail.from_name = request.POST['name']
        mail.from_email = request.POST['email']
        mail.subject = request.POST['subject']
        mail.message = request.POST['message']
        mail.save()
    return render(request, 'main/index.html', {'profile': profile})
