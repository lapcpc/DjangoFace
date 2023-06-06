from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth import logout
import json
from .models import Task


@csrf_exempt
def index(request):
    if request.method == "GET":
        return HttpResponse("Hello, world. You're at the polls index.")
    elif request.method == "POST":
        r = json.loads(request.body.decode('utf-8'))
        if request.user.is_authenticated:
            t = Task(user=request.user, task= r['task'], done=False)
            t.save()
            return HttpResponse("Task created ")
        else:
            return HttpResponse("You are not logged in", status=405)
        
@csrf_exempt
def user_tasks(request):
    if request.user.is_authenticated:
        t = Task.objects.filter(user = request.user)
        data = serializers.serialize("json",t)
        print(data) 
        return HttpResponse(data)
    else:
        return HttpResponse("user not logged in", status=405)

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        r = json.loads(request.body.decode('utf-8'))
        print(r)
        user = User.objects.create_user(r['username'], r['email'], r['password'])
        user.save() 

        return HttpResponse("User created")

@csrf_exempt
def logeo(request):
    if request.method == "POST":
        r = json.loads(request.body.decode('utf-8'))
        user = authenticate(request, username = r['username'], password = r['password'] )
        if user is not None:
            login(request, user)
            return HttpResponse("login succesfull")
        else:
            return HttpResponse("You shitted the bed man")
        
@csrf_exempt
def user(request):
    if request.method == "GET":
         if request.user.is_authenticated:
             x = request.user.username
             y = request.user.email
             z = { "name": "", "email":"" }
             z["name"]= y
             z["email"]=x
             json_data = json.dumps(z)
             print(json_data)
             return HttpResponse(json_data,  content_type="application/json")

        

def logout_view(request):
    if request.method == "GET":
        logout(request)