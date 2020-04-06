from twilio.rest import Client

my_cell = "your phone number"
my_twilio = "Your twilio number"
message = "Your message"

account_sid = "your account sid on twilio"
auth_token = "your auth_token on twilio"



client = Client(account_sid, auth_token)
client.messages.create(
  to=my_cell,
  from_=my_twilio,
  body=message)
