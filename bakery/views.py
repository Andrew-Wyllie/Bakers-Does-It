from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    context_dict = {'boldmessage': 'Love to bake!'}

    return render(request, 'bakery/index.html', context= context_dict)

def signup(request):

    context_dict = {'boldmessage': 'Sign Up'}

    return render(request, 'bakery/signup.html', context= context_dict)

def post(request):

    context_dict = {'boldmessage':'Posts'}

    return render(request, 'bakery/post.html', context=context_dict)

def search(request):
    
    context_dict = {'boldmessage':'Search'}

    return render(request, 'bakery/search.html', context=context_dict)

def question(request):

    context_dict = {'boldmessage':'Questions'}

    return render(request, 'bakery/question.html', context=context_dict)

def comment(request):

    context_dict = {'boldmessage':'Comments'}

    return render(request, 'bakery/comment.html', context=context_dict)

def login(request):

    context_dict = {'boldmessage':'Login'}

    return render(request, 'bakery/login.html', context=context_dict)

def myaccount(request):

    context_dict = {'boldmessage':'My Account'}

    return render(request, 'bakery/myaccount.html', context=context_dict)

def myquestions(request):

    context_dict = {'boldmessage':'My Questions'}

    return render(request, 'bakery/myquestions.html', context=context_dict)

def contact(request):

    context_dict = {'boldmessage':'Contact Us'}

    return render(request, 'bakery/contact.html', context=context_dict)