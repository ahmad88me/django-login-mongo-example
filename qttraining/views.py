

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from mongoengine import NotUniqueError

from django.core.servers.basehttp import FileWrapper

from datetime import datetime


@csrf_exempt
def login(request):
    print 'inside login'
    username = request.POST['username']
    password = request.POST['password']
    print 'before authentication'
    user = authenticate(username=username, password=password)
    print 'user authenticate'
    if user:
        return JsonResponse({'status': True, 'msg': 'Login successfully' })
    else:
        return JsonResponse({'status': False, 'error': 'Invalid username/password combination'})