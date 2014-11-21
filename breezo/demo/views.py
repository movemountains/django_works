from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
import json

from .forms import MyRegistrationForm

# Create your views here.


def breezo_login(request):
    token = {}
    token.update(csrf(request))
    return render_to_response('breezo_login.html', token)


def authenticate(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/breezo_loginsuccess')
 
    else:
        return HttpResponseRedirect('/breezo_loginfail')


def breezo_loginsuccess(request):
    return render_to_response('breezo_loginsuccess.html', {'first_name':request.user.username})


def breezo_loginfail(request):
    return render_to_response('breezo_loginfail.html')


def breezo_logout(request):
    return render_to_response('breezo_logout.html')


def breezo_register(request):

    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/breezo_registersuccess')

    else:
        form = MyRegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('breezo_register.html', token)


def breezo_registersuccess(request):
    return render_to_response('breezo_registersuccess.html')


# def breezo_registrationfail(request):
#     return render_to_response('breezo_registrationfail.html')

def breezo_contact(request):
     return render_to_response('breezo_contact.html')
