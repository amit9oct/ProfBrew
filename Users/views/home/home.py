from django.shortcuts import render_to_response,render
from ProfBrew.urls import EXTERNAL


def home(request):
    request.session['last_url'] = '/home/'
    request.session['call_type'] = EXTERNAL
    return render_to_response("base/base.html")

def search(request):
    return render(request,'search/home.html')