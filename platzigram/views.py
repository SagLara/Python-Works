from django.http import HttpResponse, JsonResponse

#utilities
from datetime import datetime
import json

def hello_world(request):
    """ Hola mundeishon"""
    now= datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse("Oh, hiª The current server time is {} ".format(str(now)))

def sorted(request):
    #import pdb; pdb.set_trace()3
    numbers=request.GET["numbers"].split(",")
    result=[int(num) for num in numbers]
    result.sort()
    data = {
        "status": "ok",
        "numbers": result,
        "message": "integers sorted succesfully"
    }
    #return HttpResponse(json.dumps(data, indent=4),content_type="application/json")
    return  JsonResponse(data, safe=False)

def say_hi(request,name,age):
    """Return a greeting"""
    if age<=12:
        message="Sorry {}, you are not allowed here".format(name)
    else:
        message="Hello {}, welcome to platzigram".format(name)

    return HttpResponse(message)
