from django.contrib import admin
from bucket.models import Bucket_list,To_Do,Done,Doing

 
# Register your models here.
admin.site.register(Bucket_list)
admin.site.register(To_Do)
admin.site.register(Done)
admin.site.register(Doing)



