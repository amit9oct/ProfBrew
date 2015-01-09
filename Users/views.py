from django.shortcuts import render, render_to_response
from django.http.response import *
from Users.models import Student,Professor, Branch, Users
from University.models import College
from django.template.context import *
from django.core.context_processors import *

# Create your views here.

def home(request):
    return render_to_response("base/base.html")

def login_page(request):
    return render(request,'login/login.html')

def profile(request):
    return render(request,'profile/profile.html') 

def verify_credentials(request):
    if request.method == 'GET':
        return HttpResponseBadRequest
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        tempStudent = Student.objects.filter(_username=username,_password=password)
        if len(tempStudent) == 0:
            tempProfessor = Professor.objects.filter(_username=username,_password=password)
            coursesList = tempProfessor[0].get_courses_teaching().all()
            qualificationsList = tempProfessor[0].get_qualifications().all()
            positionsList = tempProfessor[0].get_position().all()
            collegeList = College.objects.all()
            context = {'professor': tempProfessor[0],'collegeList': collegeList,'coursesList':coursesList,'qualificationsList' : qualificationsList,'positionsList' : positionsList}
            request.session['username'] = username
            request.session['user_type'] = tempProfessor[0].get_user_type()
            return render(request,'profile/professorProfile.html',context)
        elif len(tempStudent) == 1:
            yearList = []
            yearTupleList = Student.YEAR_TYPE
            for yearTuple in yearTupleList:
                x = yearTuple[1]
                yearList.append(x)
            collegeList = College.objects.all()            
            context = {'student': tempStudent[0],'collegeList': collegeList,'yearList': yearList}
            request.session['username'] = username
            request.session['user_type'] = tempStudent[0].get_user_type()
            return render(request,'profile/studentProfile.html',context)
        else:
            return HttpResponse("<html>Multiple users exists!!!!!</html>")
    
def register(request):
    college_list = College.objects.all()
    branch_list = Branch.objects.all()
    year_tupple_list = Student.YEAR_TYPE
    year_list = []
    for year_tupple in year_tupple_list:
        x=year_tupple[1]
        year_list.append(x)
    context = {'college_list': college_list,'branch_list':branch_list,'year_list': year_list}
    return render(request,'register/register.html',context)

def update(request):
    username = request.session['username']
    usertype = request.session['user_type']
    if request.method == 'GET':
        return HttpResponseBadRequest
    elif request.method == 'POST':
        if usertype == 'Student':
            if 'textName' in request.POST:
                Student.objects.filter(_username=username).update(name=request.POST['textName'])
                tempStudent = Student.objects.filter(_username=username)
                context = {'student': tempStudent[0]}
                return render(request,'profile/studentProfile.html',context)
            if 'textEmail' in request.POST:
                Student.objects.filter(_username=username).update(_email=request.POST['textEmail'])
                tempStudent = Student.objects.filter(_username=username)
                context = {'student': tempStudent[0]}
                return render(request,'profile/studentProfile.html',context) 
            if 'textPhone' in request.POST:
                Student.objects.filter(_username=username).update(_mobile_number=request.POST['textPhone'])
                tempStudent = Student.objects.filter(_username=username)
                context = {'student': tempStudent[0]}
                return render(request,'profile/studentProfile.html',context) 
            if 'sltCollege' in request.POST:
                yearList = []
                yearTupleList = Student.YEAR_TYPE
                for yearTuple in yearTupleList:
                    x = yearTuple[0]
                    yearList.append(x)
                collegeList = College.objects.all()
                clg = College.objects.filter(college_name=request.POST['sltCollege'])
                Student.objects.filter(_username=username).update(_college=clg[0])
                tempStudent = Student.objects.filter(_username=username)
                context = {'student': tempStudent[0],'collegeList': collegeList,'yearList': yearList}
                return render(request,'profile/studentProfile.html',context)
            if 'sltYear' in request.POST:
                yearList = []
                yearTupleList = Student.YEAR_TYPE
                numYear = 0
                for yearTuple in yearTupleList:
                    x = yearTuple[1]
                    yearList.append(x)
                    if yearTuple[1] == request.POST['sltYear']:
                        numYear = yearTuple[0]
                collegeList = College.objects.all()
                Student.objects.filter(_username=username).update(_year=numYear)
                tempStudent = Student.objects.filter(_username=username)
                context = {'student': tempStudent[0],'collegeList': collegeList,'yearList': yearList}
                return render(request,'profile/studentProfile.html',context)
            if 'textDegree' in request.POST:
                Student.objects.filter(_username=username).update(_degree_pursued=request.POST['textDegree'])
                tempStudent = Student.objects.filter(_username=username)
                context = {'student': tempStudent[0]}
                return render(request,'profile/studentProfile.html',context)
            
def register_student(request):
    if request.method == 'GET':
        return render("<html>Bad way to access!!!!</html>")
    elif request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        name = fname+' '+lname
        email = request.POST['email']
        password = request.POST['password']
        clgname = request.POST['clgname']
        branch_name = request.POST['branch']
        degree = request.POST['degree']
        year = request.POST['year']
        year_tupple_list = Student.YEAR_TYPE
        num_year = 0
        for year_tupple in year_tupple_list:
            if year_tupple[1] == year:
                num_year = year_tupple[0]
        branch_list = Branch.objects.filter(_branch_name=branch_name)
        clg_list = College.objects.filter(college_name=clgname)
        clg=clg_list[0]
        branch=branch_list[0]
        Student.objects.create(_username=username,user_type=Users.STUDENT,_password=password,name=name,_email=email,_college=clg,_contributing_factor=0,_branch=branch,_degree_pursued=degree,_year=num_year)
        return login_page(request)

def username_present(request):
    username = request.POST.get('username',None)
    user_type = request.POST.get('user_type',None)
    if user_type=='Student':
        tempObj = Student.objects.filter(_username=username)
        if len(tempObj) != 0:
            return HttpResponse("User Name already exists")
        else:
            return HttpResponse("False")
    else:
        tempObject = Professor.objects.filter(_username=username)
        if len(tempObject) != 0:
            return HttpResponse("User Name already exists")
        else:
            return HttpResponse("False")   