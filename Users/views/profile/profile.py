from Users.models import Student, Professor
from University.models import College
from django.shortcuts import render
from Ratings.models import ProfRatings

def profile(request,user_type):
    temp_username = request.session['username'] 
    temp_user = None
    if user_type == 'Student':
        temp_user = Student.objects.filter(_username=temp_username)
        yearList = []
        yearTupleList = Student.YEAR_TYPE
        for yearTuple in yearTupleList:
            x = yearTuple[1]
            yearList.append(x)
        collegeList = College.objects.all()            
        context = {'student': temp_user[0],'collegeList': collegeList,'yearList': yearList}
        return render(request,'profile/editStudentProfile.html',context)
    elif user_type == 'Professor':
        temp_user = Professor.objects.filter(_username=temp_username)
        coursesList = temp_user[0].get_courses_teaching().all()
        qualificationsList = temp_user[0].get_qualifications().all()
        positionsList = temp_user[0].get_position().all()
        collegeList = College.objects.all()
        rateList = ProfRatings.objects.filter(_prof =  temp_user[0])
        context = {'professor': temp_user[0],'collegeList': collegeList,'coursesList':coursesList,'qualificationsList' : qualificationsList,'positionsList' : positionsList,'rate' : rateList[0]}
        return render(request,'profile/editProfessorProfile.html',context)

def profile_of_prof(request,prof_id,user_type):
        temp_user = Professor.objects.filter(_username = prof_id)
        coursesList = temp_user[0].get_courses_teaching().all()
        qualificationsList = temp_user[0].get_qualifications().all()
        positionsList = temp_user[0].get_position().all()
        collegeList = College.objects.all()
        rateList = ProfRatings.objects.filter(_prof = prof_id)
        rate = rateList[0]
        context = {'professor': temp_user[0],'collegeList': collegeList,'coursesList':coursesList,'qualificationsList' : qualificationsList,'positionsList' : positionsList,'rate' : rate}
        return render(request,'profile/professorProfile.html',context)