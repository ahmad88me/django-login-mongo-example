

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
from models import *


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


@csrf_exempt
def chat(request):
    name = request.POST['name']
    text = request.POST['text']
    c = Chat()
    c.name = name
    c.text = text
    c.sent_on = datetime.now()
    c.save()
    return JsonResponse({'status': True, 'chat': get_latest_chats()})


@csrf_exempt
def get_chat(request):
    return JsonResponse({'status': True, 'chat': get_latest_chats()})


def get_latest_chats():
    chat_objs = Chat.objects.all()
    chat = []
    for c in chat_objs:
        chat.append({'name': c.name, 'text': c.text, 'sent_on': c.sent_on})
    #return sorted(chats,key=lambda c: c.sent_on, reverse=True)
    chat.sort(key=lambda c: c['sent_on'], reverse=True)
    chat = chat[:15]
    chat.sort(key=lambda c: c['sent_on'], reverse=False)
    return chat