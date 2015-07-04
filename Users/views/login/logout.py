'''
Created on Mar 1, 2015

@author: Amitayush Thakur
'''
from Users.models import Branch
from django.shortcuts import render
from django.http.response import HttpResponse

def logout(request):
    request.session.flush()
    msg = 'Successfully Logged Out!!!'
    title = 'Logged Out'
    otherdata = "<a href='/home/'>Click here to go back!!</a>"
    branch_list = Branch.objects.all()
    context = { 'message':msg , 'otherdata':otherdata,'title':title,'branch_list':branch_list}
    return render(request,'error.html',context)