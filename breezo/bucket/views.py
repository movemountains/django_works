from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
from .models import Bucket_list
from .forms import BucketForm

def bucket(request):
   form = BucketForm(request.POST or None)
   if form.is_valid():
       save_post = form.save()
   #  return HttpResponse( "bucket.html")
   return render_to_response('bucket.html')
