from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

import send_sms

app = Flask(__name__)

@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    location = request.values.get('Body', None)
    contact = request.values.get('From', None)
    
    res = send_sms.send_sms(location, contact)
       
    resp = MessagingResponse()
    resp.message(res)
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)