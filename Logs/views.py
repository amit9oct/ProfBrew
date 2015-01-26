from django.shortcuts import render
import Users.views
from ProfBrew.urls import INTERNAL
from Logs.models import ProfLog
from Users.models import Professor, Student
from Ratings.views.basic.rate_prof import LIKES, DISLIKES, DONT_KNOW
from Ratings.models import ProfRatings
from django.http.response import HttpResponseBadRequest, HttpResponse
# Create your views here.

def update_prof_log(request,prof_log,prof_rate,opcode):
    if opcode == LIKES:                                         #Validation statements to check if already there or not
        prof_log.update_like(True)
        if prof_log.get_dislike() == 'True' :
            prof_log.update_dislike(False)
            prof_rate.update_likes(prof_rate.get_likes()+1)
            prof_rate.update_dislikes(prof_rate.get_dislikes()-1)
        elif prof_log.get_dont_know() == 'True' :
            prof_log.update_dont_know(False)
            prof_rate.update_likes(prof_rate.get_likes()+1)
    elif opcode == DISLIKES:
        prof_log.update_dislike(True)
        if prof_log.get_like() == 'True':
            prof_log.update_like(False)
            prof_rate.update_dislikes(prof_rate.get_dislikes()+1)
            prof_rate.update_likes(prof_rate.get_likes()-1)
        elif prof_log.get_dont_know() == 'True':
            prof_log.update_dont_know(False)
            prof_rate.update_dislikes(prof_rate.get_dislikes()+1)
    elif opcode == DONT_KNOW:
        prof_log.update_dont_know(True)
        if prof_log.get_like() == 'True':
            prof_log.update_like(False)
            prof_rate.update_likes(prof_rate.get_likes()-1)
        elif prof_log.get_dislike() == 'True':
            prof_log.update_dislike(False)
            prof_rate.update_dislikes(prof_rate.get_dislikes()-1)
    #if prof_log.is_valid_log():
    prof_log.save()
    prof_rate.assign_rate()
    prof_rate.save()
    
def update_log(request,student_id,prof_id,opcode):
    if request.session['user_type'] == 'Student':
        if request.session['username'] ==  student_id :
            #Allow the person to rate
            #Update logs
            student_list = Student.objects.filter(_username = student_id)
            prof_list = Professor.objects.filter(_username = prof_id)
            prof_rate_list = ProfRatings.objects.filter(_prof = prof_list[0])
            prof_log_list = ProfLog.objects.filter(_student = student_list[0],_professor = prof_list[0] )
            if len(prof_log_list) == 0:
                prof_log = ProfLog.objects.create(_student = student_list[0],_professor = prof_list[0])
                prof_rate = prof_rate_list[0] #Here object is made because list is immutable and no change can be made with prof_list_rate[0]
                if opcode == LIKES: 
                    prof_rate.likes()
                    prof_log.update_like(True)
                elif opcode == DISLIKES:
                    prof_rate.dislikes()
                    prof_log.update_dislike(True)
                else:
                    prof_log.update_dont_know(True)
                prof_log.save()
                prof_rate.assign_rate()
                prof_rate.save()
            else:
                prof_log = prof_log_list[0]
                update_prof_log(request,prof_log,prof_rate_list[0],opcode)
            request.session['call_type'] = INTERNAL
            request.session['mnemonics'] = 'PROF_PROFILE_VIEW/'+prof_id
            return Users.views.caller.caller(request)
        else:
            return HttpResponseBadRequest
    else:
        return HttpResponseBadRequest