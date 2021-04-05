from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect
from bakery.models import Category
from bakery.models import Page
from bakery.forms import UserForm, UserProfileForm

def index(request):

    category_list = Category.objects

    context_dict = {}
    context_dict['boldmessage'] =  'Love to bake!'
    context_dict['categories'] = category_list

    return render(request, 'bakery/index.html', context= context_dict)

def register(request):
    
    registered = False

    if request.method == 'POST':
 
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)


        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:

            print(user_form.errors, profile_form.errors)
    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'bakery/signup.html' , context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

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

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return redirect(reverse('rango:index'))
            else:

                return HttpResponse("Your Bakers Does It account is disabled.")
        
        else:

            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")


    else:

        return render(request, 'bakery/login.html')

def myaccount(request):

    context_dict = {'boldmessage':'My Account'}

    return render(request, 'bakery/myaccount.html', context=context_dict)

def myquestions(request):

    context_dict = {'boldmessage':'My Questions'}

    return render(request, 'bakery/myquestions.html', context=context_dict)

def contact(request):

    context_dict = {'boldmessage':'Contact Us'}

    return render(request, 'bakery/contact.html', context=context_dict)

def show_category(request, category_name_slug):

    context_dict = {}
    
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    
    return render(request, 'bakery/category.html')