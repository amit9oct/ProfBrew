from django.db import models
from Users.models import Professor,Student,DEFAULT_FIELD_VALUE,College,Branch
# Create your models here.
MAX_LENGTH_OF_REVIEW = 2000

class Reviews(models.Model):
    """
    Abstract class for inheritance in professor, college and branch review class
    """
    _review = models.CharField(max_length=MAX_LENGTH_OF_REVIEW,default=DEFAULT_FIELD_VALUE,null=True)
    class Meta:
        abstract = True
    
class ProfessorReviews(Reviews):
    """
    _professor = Foreign key established with Professor class in app Users
    _student = Foreign key established with Student class in app Users
    """
    def __str__(self):    
        return str(self._professor)+'-'+str(self._student)
    _professor = models.ForeignKey(Professor,default=DEFAULT_FIELD_VALUE,null=False)
    _student = models.ForeignKey(Student,default=DEFAULT_FIELD_VALUE,null=False)

class CollegeReviews(Reviews):
    """
    _college = Foreign key established with College class in app Users
    _student = Foreign key established with Student class in app Users
    """
    def __str__(self):    
        return str(self._college)+'-'+str(self._student)
    _college = models.ForeignKey(College,default=DEFAULT_FIELD_VALUE,null=False)
    _student = models.ForeignKey(Student,default=DEFAULT_FIELD_VALUE,null=False)

class BranchReviews(Reviews):
    """
    _branch = Foreign key established with Branch class in app Users
    _student = Foreign key established with Student class in app Users
    """
    def __str__(self):    
        return str(self._branch)+'-'+str(self._student)
    _branch = models.ForeignKey(Branch,default=DEFAULT_FIELD_VALUE,null=False)
    _college = models.ForeignKey(College,default=DEFAULT_FIELD_VALUE,null=False)
    _student = models.ForeignKey(Student,default=DEFAULT_FIELD_VALUE,null=False)
