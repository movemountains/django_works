from django.contrib import admin
from bucket.models import BucketList,To_Do,Done,Doing

 
# Register your models here.
admin.site.register(BucketList)
admin.site.register(To_Do)
admin.site.register(Done)
admin.site.register(Doing)



