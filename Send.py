from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACce7ca982c8ee3a79f64bb9082ead98a0'
auth_token = 'e6e1d7e1bb4cd13e91ee6bc4a7fd1ce8'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='Twilio Number',
                              body='body',
                              to='Revciever Number'
                          )



print(message.sid)

