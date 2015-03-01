'''
Created on Mar 1, 2015

@author: Amitayush Thakur
'''
import Users.views
from Users.models import Student, Users, Professor, Branch
from random import randint
from University.models import College
from django.http.response import HttpResponse
from Ratings.views.basic.rate_prof import rate_prof, LIKES, DISLIKES, DONT_KNOW
from Ratings.models import ProfRatings
from Logs.views import update_log
from Reviews.views.add_reviews import add_prof_review, REVIEW_TYPE, FRESH_REVIEW,\
    EXISTING_REVIEW
from Reviews.models import BranchReviews, CollegeReviews
from ProfBrew.urls import INTERNAL, APPLICATION
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from Users.views.login.logout import logout
from survey.models import OtherDetails
#Some important parameters
CLG_NAME = 'BITS Pilani Pilani Campus'
DEFAULT_YEAR = 5

def survey_home(request):
    branch_list = Branch.objects.all()
    context = {'branch_list':branch_list}
    return render(request,'survey/home.html',context)

def survey(request):
    clg = College.objects.filter(college_name = CLG_NAME)[0]
    branch_text = request.GET['branch']
    branch = Branch.objects.filter(_branch_name = branch_text)[0]
    prof_list = Professor.objects.filter(_branch=branch,_college=clg)
    context={'college':clg,'branch':branch,'prof_list':prof_list}
    return render(request,'survey/survey.html',context)
    
def createStudent(request,email,degree,branch):
    raw_username = email.split("@")
    username_base = raw_username[0]
    email_base = raw_username[1].split(".")
    email_domain = email_base[0]
    username = username_base + email_domain
    user_count = Student.objects.filter(_username=username).count()
    if user_count == 0:
        password =  username + str(randint(0,1000000))
        num_year = DEFAULT_YEAR
        clg = College.objects.filter(college_name=CLG_NAME)[0]
        Student.objects.create(_username = username,_password = password,user_type=Users.STUDENT,name=username,_email=email,_college=clg,_contributing_factor=0,_branch=branch,_degree_pursued=degree,_year=num_year)
        return str(username)+'&'+str(password)
    else:
        return HttpResponse("Multiple Accounts not allowed!!!")
    
def likeDislike(request,student_id,prof_id,op_code):
    student_list = Student.objects.filter(_username = student_id)
    """
        Set session for the newly created student
    """
    if len(student_list) == 1:
        request.session['username'] = student_id
        request.session['call_type'] = APPLICATION
        if op_code == 'LIKES':
            update_log(request,student_id,prof_id,LIKES)
        elif op_code == 'DISLIKES':
            update_log(request,student_id,prof_id,DISLIKES)
        else:
            update_log(request, student_id, prof_id,DONT_KNOW)
    prof_list = Professor.objects.filter(_username = prof_id)
    prof_rate_list = ProfRatings.objects.filter(_prof = prof_list[0])
    prof_rate = prof_rate_list[0]
    return HttpResponse(prof_rate.__str__())

def addProfReview(request,student_id,prof_id,review_text):
    student_list= Student.objects.filter(_username = student_id)
    if len(student_list) == 1:
        request.session['username'] = student_id
        request.session['call_type'] = APPLICATION
        return add_prof_review(request,prof_id,student_id,None,REVIEW_TYPE['Fresh Review'],review_text)
    else:
        return HttpResponse("Can't add more than one review using!!!")
    
def addBranchReview(request,branch_text,student_id,review_id,review_type,review_text):
    student_list = Student.objects.filter(_username = student_id)
    student = student_list[0]
    clg = College.objects.filter(college_name=CLG_NAME)[0]
    branch = Branch.objects.filter(_branch_name = branch_text)[0]
    if len(student_list) == 1:
        request.session['username'] = student_id
        if review_type == FRESH_REVIEW:
            new_review = BranchReviews.objects.create(_branch=branch,_student=student,_review=review_text,_college=clg)
        elif review_type == EXISTING_REVIEW:
            new_review = BranchReviews.objects.create(_branch=branch,_student=student,_review=review_text,_college=clg)
            prev_review =BranchReviews.objects.filter(_review_id=review_id)[0]
            prev_review.update_next_review(new_review)
            prev_review.save()
    return HttpResponse(review_text)

def clgReview(request,student_id,review_id,review_type,review_text):
    clg = College.objects.filter(college_name=CLG_NAME)[0]
    student_list = Student.objects.filter(_username = student_id)
    student = student_list[0]
    if len(student_list) == 1:
        request.session['username'] = student_id
        if review_type == FRESH_REVIEW:
            new_review = CollegeReviews.objects.create(_college=clg,_student=student,_review=review_text)
        elif review_type == EXISTING_REVIEW:
            new_review = CollegeReviews.objects.create(_college=clg,_student=student,_review=review_text)
            prev_review =CollegeReviews.objects.filter(_review_id=review_id)[0]
            prev_review.update_next_review(new_review)
            prev_review.save()
    return HttpResponse(review_text)

@csrf_exempt
def survey_submit(request):
    if request.method == 'POST':
        email = request.POST['email']
        branch_text = request.POST['branch']
        branch = Branch.objects.filter(_branch_name=branch_text)[0]
        student_details = createStudent(request,email,'B Tech',branch).__str__()
        if len(student_details.split('&'))==1 :
            return HttpResponse("Multiple submissions not allowed!!!")
        username = student_details.split('&')[0]
        password = student_details.split('&')[1]
        request.session['username'] = username
        request.session['user_type'] = 'Student'
        clg = College.objects.filter(college_name=CLG_NAME)[0]
        prof_list = Professor.objects.filter(_branch=branch,_college=clg)
        for prof in prof_list:
            likeDislike(request, username, prof.get_username(),request.POST['optradio'+prof.get_username()])
            addProfReview(request,username,prof.get_username,request.POST['profReview'+prof.get_username()])
        addBranchReview(request, branch_text, username,None,REVIEW_TYPE['Fresh Review'], request.POST['branchReview'])
        clgReview(request,username,None,REVIEW_TYPE['Fresh Review'], request.POST['clgReview'])
        OtherDetails.objects.create(_email=email,_job_satisfaction=request.POST['jobOpp'],_research_avenues=request.POST['resAv'],\
                                    _job_satisfaction_rate=request.POST['optradioJobOpp'],\
                                    _research_avenues_rate=request.POST['optradioResAv'],
                                    _college_review_rate=request.POST['optradioClgReview'])
        logout(request)
        return HttpResponse("Congrats <a href='/search/?txtSearch=&search_type=Professor'>Click here to view results!!</a>")
    else:
        return HttpResponse("Not Accessible this way!!!")