from twilio.rest import Client
import smtplib
account_sid = "xXx"
auth_token = "xXx"
my_email = "xXx@gmail.com"
password = "xXx"



class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)
        self.connection = smtplib.SMTP("smtp.gmail.com",25)

    def send_sms(self, message_body):

        message = self.client.messages.create(
            from_="+xXx",
            body=message_body,
            to="+xXx"
        )
        print(message.sid)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:+xXx',
            body=message_body,
            to=f'whatsapp:+xXx'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection as connections:
            connections.starttls()
            connections.login(my_email,password)
            for email in email_list:
                connections.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}"
                )
