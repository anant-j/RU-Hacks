import requests
import json
from . import API_KEYS
#from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse

class TwilioAPIClass:
    def __init__(self):
        self.account_sid = API_KEYS.keys['MY_ACCOUNT_SID']
        self.auth_token = API_KEYS.keys['MY_AUTH_TOKEN']
        self.twilio_number = API_KEYS.keys['MY_TWILIO_NUMBER']
        self.my_number = API_KEYS.keys['MY_PHONE_NUMBER']
        

    def send_verification_code(self, number):
        account_sid = self.account_sid
        auth_token = self.auth_token
        client = Client(account_sid, auth_token)

        verification = client.verify \
                                 .services(API_KEYS.keys['SERVICE_ID']) \
                                 .verifications \
                                 .create(to="+1"+number, channel='sms')
        
        return(verification.sid)



    def check_verification_code(self, code):
        from twilio.rest import Client
        account_sid = 'AC0c978ddce5d486d0f450280824dff05f'
        auth_token = '87f8484897b86df395bcac2c6dbf5e48'
        client = Client(account_sid, auth_token)
        
        verification_check = client.verify \
            .services('VAcd7b5eb82f7f8f4b3633139938f79ed0') \
            .verification_checks \
            .create(to='+1'+"2892103288", code=code)
        
        return verification_check.sid

    def sms(self):
        from twilio.rest import Client
        client = Client(self.account_sid, self.auth_token)
        
        client.messages.create(
                to = "+16477710786",
                from_ = "16479330080",
                body = "hi"
        )
    
    def sms_reply(self):
        pass
        
        
if __name__ == '__main__':
    a = TwilioAPIClass()
    a.sms()

    