''' Exercicio do dia 35 '''

from twilio.rest import Client


conta_sid = "AC895a73e7c37076a710082239d691a073"
token = "5fd57bc147b329f68b1463ce588a37e0"
client = Client(conta_sid, token)

message = client.messages \
                .create(
                        body="Hello World, muito legal essa função",
                        from_='+16072988448',
                        to='+5511985945738'
                )

print(message.sid)
