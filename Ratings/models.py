from django.db import models
from Users.models import Professor,DEFAULT_FIELD_VALUE



WT_OF_LIKES=0.5
WT_OF_QUALIFICATIONS=0.5
# Create your models here.
class Ratings(models.Model):
    _no_of_likes=models.BigIntegerField(null=False,default=DEFAULT_FIELD_VALUE)
    class Meta:
        abstract=True

class ProfRatings(Ratings):
    _prof=models.ForeignKey(Professor,null=False,default=DEFAULT_FIELD_VALUE)
    _rate=models.BigIntegerField(null=False,default=0)
    def __str__(self):
        self.assign_rate()
        self.save()
        return self._prof.name+'-'+str(self._rate)
    def assign_rate(self):
        self._rate=WT_OF_LIKES*self._no_of_likes+WT_OF_QUALIFICATIONS*self._no_of_likes*self._prof.get_qualifications().number_of_qualifications
    