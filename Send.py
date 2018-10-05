from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'Get From Twilio Consol'
auth_token = 'Get From Twilio Consol'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='Twilio Number',
                              body='body',
                              to='Revciever Number'
                          )



print(message.sid)

