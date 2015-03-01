'''
Created on Jan 26, 2015

@author: Amitayush Thakur
'''
from Reviews.models import ProfessorReviews
from Users.models import Professor, Student
from django.http.response import HttpResponse
import Users.views
from ProfBrew.urls import INTERNAL, APPLICATION
import json

FRESH_REVIEW = 1
EXISTING_REVIEW = 2
REVIEW_TYPE = {
    'Fresh Review':FRESH_REVIEW,
    'Existing Review':EXISTING_REVIEW,
}

def add_prof_review(request,prof_id,student_id,review_id,review_type,review_text):
    prof = Professor.objects.filter(_username=prof_id)[0]
    student = Student.objects.filter(_username=student_id)[0]
    if review_type == FRESH_REVIEW:
        new_review = ProfessorReviews.objects.create(_professor=prof,_student=student,_review=review_text)
        if request.session['call_type'] == APPLICATION:
            response_data= {}
            response_data['message'] = review_text
            return HttpResponse(json.dumps(response_data),"application/json")
        request.session['call_type'] = INTERNAL
        request.session['mnemonics'] = 'PROF_PROFILE_VIEW/'+ prof_id
        return Users.views.caller.caller(request)
    elif review_type == EXISTING_REVIEW:
        new_review = ProfessorReviews.objects.create(_professor=prof,_student=student,_review=review_text)
        prev_review = ProfessorReviews.objects.filter(_review_id=review_id)[0]
        prev_review.update_next_review(new_review)
        prev_review.save()
    return HttpResponse(review_text)

