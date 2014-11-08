from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages

# Create your views here.
from .models import Bucket_list
from .forms import BucketForm

def bucket(request):
    form = BucketForm(request.POST or None)
    return render_to_response("bucket.html",locals(),
                               context_instance=RequestContext(request))
