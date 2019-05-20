from django.shortcuts import render
from django.http import HttpResponse
from . import TwilioAPI
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    if request.method == 'POST':
        data = request.POST.copy()
        number = data.get('phone')
    
        if len(number) != 10:
            message = "Invalid phone number provided."
            return render(request, 'index.html', {'message':message})
        else:
            t = TwilioAPI.TwilioAPIClass()
            sid = t.send_verification_code(number)
            data = {
                'sid':sid, 'number':number,
                    }
            return render(request, 'verify.html', {'data':data})
            
            
        return render(request, 'index.html', {'number':number})
    
    else:
        return render(request,'index.html')
    
def verify(request):
    if request.method == "POST":
        data = request.POST.copy()
        verification_code = data.get('verify')
        
        t = TwilioAPI.TwilioAPIClass()
        sid = t.check_verification_code(verification_code)  
        return render(request, 'index.html', {'sid':sid})
    else:
        return HttpResponse("verify page")

@csrf_exempt
def sms_reply(request):
    if request.method == "POST":
        twiml = '<Response><Message>Hello from your Django app!</Message></Response>'
        return HttpResponse(twiml, content_type='text/xml')
    return HttpResponse('hi')