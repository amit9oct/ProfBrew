from django.contrib import admin
from Reviews.models import ProfessorReviews, CollegeReviews, BranchReviews

# Register your models here.
admin.site.register(ProfessorReviews)
admin.site.register(CollegeReviews)
admin.site.register(BranchReviews)