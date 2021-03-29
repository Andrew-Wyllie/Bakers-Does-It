from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bakers Does It Yall!!")

def signup(request):
    return HttpResponse("sign up page")

def post(request):
    return HttpResponse("posts page")

def search(request):
    return HttpResponse("Search Page")

def question(request):
    return HttpResponse("Question Page")

def comment(request):
    return HttpResponse("Comment page")

def login(request):
    return HttpResponse("Login page")

def myaccount(request):
    return HttpResponse("My Account")

def myquestions(request):
    return HttpResponse("My Questions")

def contact(request):
    return HttpResponse("Contact Page.")