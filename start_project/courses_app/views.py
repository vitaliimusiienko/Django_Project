from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def courses(request):
    text = {
            'authorized': 'This is the Courses page',
            'unautorized': 'You have no permissions to view this page'
            }
    if request.user.is_authenticated:
            return HttpResponse(text['authorized'])
    else:
            return HttpResponse(text['unautorized'])