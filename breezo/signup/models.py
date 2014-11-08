from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.


class SignUp (models.Model):
    first_name=models.CharField(max_length=120, null=True, blank=True)
    last_name=models.CharField(max_length=120, null=True, blank=True)
   # phone= models.CharField(max_length=100)
   # city=models.ForeignKey(City,related_name='city', blank=True, null=True, help_text=_('Select your City'))
   # location=models.ForeignKey(Country,related_name='location', blank=True, null=True, help_text=_('Select your Location'))
    email=models.EmailField()
    
    def __unicode__(self):
        return smart_unicode(self.email)
