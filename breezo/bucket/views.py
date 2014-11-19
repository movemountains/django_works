from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
from .forms import BucketListForm,To_DoForm,DoneForm,DoingForm
from .models import BucketList,To_Do,Done,Doing


def bucket(request):
    form = BucketListForm(request.POST or None)
    if form.is_valid():
       save_post = form.save()
   #  return HttpResponse( "bucket.html")
    return render_to_response('bucket.html',locals(),context_instance=RequestContext(request))


def todo(request):
    form = To_DoForm(request.POST or None)
    if form.is_valid():
        save_post = form.save()
    return render_to_response("todo.html",locals(),context_instance=RequestContext(request))


def done(request):
    form = DoneForm(request.POST or None)
    if form.is_valid():
        save_post = form.save()
    return render_to_response("done.html",locals(),context_instance=RequestContext(request))


def doing(request):
    form = DoingForm(request.POST or None)
    if form.is_valid():
        save_post = form.save()
    return render_to_response("doing.html",locals(),context_instance=RequestContext(request))