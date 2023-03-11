from twilio.rest import Client

account_sid = 'AC93b6b5b901b6926a009d1184d5eaa881'
auth_token = 'Redacted'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG2f32d9428ea339b26b7c0bd3f62dd63b',
    body='Hellloooo',
    to='+256788952922'
)

print(message.sid)
