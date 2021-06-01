
from smtplib import SMTP

try:
    sender_email = "Nathandj28@gmail.com"
    receiver_email = "Nathandj28@gmail.com"
    password = input(str("Please enter your password"))
    server = SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender_email, password )
    server.sendmail(sender_email, receiver_email, 'This is a test email.')
    print("the message has been successfully sent")

except Exception as err:
    print("Something went wrong..", err)
finally:
    server.close()
