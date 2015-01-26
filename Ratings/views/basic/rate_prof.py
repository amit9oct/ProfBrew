'''
Created on Jan 20, 2015

@author: Amitayush Thakur
'''
from Ratings.models import ProfRatings
from Users.models import Professor, Student
import Users.views
from ProfBrew.urls import INTERNAL
from django.http.response import HttpResponse
from Logs.models import ProfLog

LIKES = 1
DISLIKES = 2
DONT_KNOW = 3
OP_CODE={(LIKES,'Likes'),(DISLIKES,'Dislikes'),(DONT_KNOW,'Dont_know')}

def rate_prof(request,prof_id,op_code):
    prof = Professor.objects.filter(_username = prof_id)
    prof_rate_list = ProfRatings.objects.filter(_prof = prof[0])
    prof_rate = prof_rate_list[0]
    if op_code  == LIKES:
        prof_rate.likes()
    elif op_code == DISLIKES :
        prof_rate.dislikes()
    prof_rate.assign_rate()
    prof_rate.save()
    current_rate = prof_rate.__str__()
    request.session['call_type'] = INTERNAL
    request.session['mnemonics'] = 'PROF_PROFILE_VIEW/'+prof_id
    return Users.views.caller.caller(request)
    #return HttpResponse(current_rate)
        