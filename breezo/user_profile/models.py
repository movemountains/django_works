from django.db import models

class user_profile(models.Model):
    email=models.EmailField()

    def __unicode__(self):
        return smart_unicode(self.email)



# Create your models here.
