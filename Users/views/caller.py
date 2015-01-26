'''
Created on Jan 10, 2015

@author: Amitayush Thakur,Sagar Grover and Abhimanyu Siwach
'''
from Users.views.login.login import login
from Users.views.login.login import verify_credentials
from Users.views.home.home import home
from django.core.context_processors import *
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.http.response import HttpResponse
from Users.views.register.register import register, username_present,\
    register_student
from ProfBrew.urls import INTERNAL, EXTERNAL, mnemonics
from Users.views.profile.profile import profile, profile_of_prof
from Users.views.profile.update import update
from Ratings.views.basic.rate_prof import rate_prof, LIKES, DISLIKES, DONT_KNOW
from Logs.views import update_log
"""
This module is God Of Everything :P

"""

@csrf_exempt 
def caller(request):
    array = None
    if not 'call_type' in request.session:
        request.session['call_type'] = EXTERNAL
    call_type = request.session['call_type']
    if call_type  == INTERNAL:
        array = str(request.session['mnemonics']).split('/')
        request.session['call_type'] = EXTERNAL
    elif call_type == EXTERNAL:
        if request.method == 'POST':
            array = str(request.POST['mnemonics']).split('/')
        if request.method == 'GET':
            array = str(request.POST['mnemonics']).split('/')
    mnemonics = array[0]
    if mnemonics == None:
        return home(request)
    if mnemonics == 'HOME':
        return home(request)
    if mnemonics == 'LOGIN_PAGE':
        return login(request)
    if mnemonics == 'VERIFY_CRED':
        last_url = request.session['last_url']
        user_type = request.POST['user_type']
        request.session['mnemonics'] = 'VERIFY_CRED'
        return verify_credentials(request,user_type,last_url)
    if mnemonics == 'REGISTER_STUDENT':
        return register_student(request)
    if mnemonics == 'USER_PRESENT' :
        request.session['mnemonics'] = 'USER_PRESENT'
        return username_present(request)
    if mnemonics == 'PROFILE_VIEW':
        user_type = request.session['user_type']
        return profile(request,user_type)
    if mnemonics == 'PROF_PROFILE_VIEW':
        user_type = 'Professor'
        prof_id = array[1]
        return profile_of_prof(request,prof_id,user_type) 
    if mnemonics == 'UPDATE_PROFILE':
        return update(request)
    if mnemonics == 'LIKE':         #Can be called only externally
        student_id = request.session['username']
        prof_id = request.POST['prof_id']
        return update_log(request,student_id,prof_id,LIKES) #to be changed later
    if mnemonics == 'DISLIKE':      #Can be called only externally
        student_id = request.session['username']
        prof_id = request.POST['prof_id']
        return update_log(request,student_id,prof_id,DISLIKES)  #to be changed later
    if mnemonics == 'DONT_KNOW':    #Can be called only externally
        student_id = request.session['username']
        prof_id = request.POST['prof_id']
        return update_log(request,student_id,prof_id,DONT_KNOW)  #to be changed later
    if mnemonics == 'RATE_PROF':
        opcode = array[1]
        return rate_prof(request,prof_id,opcode)  #to be changed later
    return HttpResponse(str(call_type)+' '+str(mnemonics))