'''
Created on Mar 1, 2015

@author: Amitayush Thakur
'''
from django.http.response import HttpResponse

def logout(request):
    request.session.flush()
    return HttpResponse("You have logged Out!!<a href='/home/'>Click here to go back</a>")