from twilio.rest import Client
account_sid = "private"
auth_token = "private"



class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message_body):

        message = self.client.messages.create(
            from_="private",
            body=message_body,
            to="private"
        )
        print(message.sid)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:private',
            body=message_body,
            to=f'whatsapp:private'
        )
        print(message.sid)
