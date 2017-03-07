from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404


from .models import users

import datetime

from .forms import RegForm

def welcome(request):
    template = loader.get_template('registration/index.html')
    return HttpResponse(template.render(request))

def register(request):
    template = loader.get_template('registration/register.html')
    template_email = loader.get_template('registration/email.html')
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            request.session['email'] = request.POST['email']
            return HttpResponseRedirect(reverse('registration:email'))
    else:
        form = RegForm()
    context = { 'form' : form, }
    return HttpResponse(template.render(context, request))

def email_confirm(request):
    template = loader.get_template('registration/email.html')
    email = request.session.get('email')
    send_mail('Welcome-to-Bioinfo-Workshop','Good-Day','rajeshs@cdac.in',[email],
            fail_silently=False,)
    return HttpResponse(template.render(request))

def registerdb(request):
    template = loader.get_template('registration/register.html')
    template_email = loader.get_template('registration/email.html')
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            request.session['email'] = request.POST['email']
            users.objects.create(name=form.cleaned_data['your_good_name'],
                    email=form.cleaned_data['email'],
                    birthdate=form.cleaned_data['date_of_birth'],
                    reg_date=datetime.datetime.now(),
                    group=form.cleaned_data['group'],
                    slot=form.cleaned_data['session_id'],
                    )
            return HttpResponseRedirect(reverse('registration:email'))
    else:
        form = RegForm()
    context = { 'form' : form, }
    return HttpResponse(template.render(context, request))

def users_list(request):
    user_list = users.objects.all()
    return render(request, 'registration/users.html',  {'user_list': user_list})
    
