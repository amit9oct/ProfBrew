from django.http.response import HttpResponse
from Users.models import Professor
from Ratings.models import ProfRatings
from django.shortcuts import render
from Users.views.profile.profile import profile_of_prof

def prof_profile(request):
    prof_id = request.GET['prof']
    return profile_of_prof(request,prof_id,None)