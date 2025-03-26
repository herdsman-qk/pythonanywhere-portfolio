from django.shortcuts import render
from .models import *

# Create your views here.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender_email, receiver_email, subject, body, password):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the email body to the email message
    message.attach(MIMEText(body, 'plain'))

    # Set up the server and send the email
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Encrypt the connection

        # Log in to your Gmail account
        server.login(sender_email, password)

        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")

    finally:
        # Close the connection
        server.quit()


def index(request):
    profile = Profile.objects.all()[0]
    if request.method == "POST":
        mail = MyMail()
        mail.from_name = request.POST['name']
        mail.from_email = request.POST['email']
        mail.subject = request.POST['subject']
        mail.message = request.POST['message']
        mail.save()
    return render(request, 'main/index.html', {'profile': profile})
