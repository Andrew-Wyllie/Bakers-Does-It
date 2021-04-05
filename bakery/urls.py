from django.urls import path
from bakery import views

app_name = 'bakery'

urlpatterns = [
    path('', views.index, name='index'),

    path('signup/', views.register, name='signup'),

    path('post/', views.post, name='post'),

    path('search/', views.search, name='search'),
    path('search/question/', views.question, name='question'),
    path('search/question/comment/', views.comment, name='comment'),

    path('login/', views.user_login, name='login'),
    path('login/myaccount/', views.myaccount, name='myaccount'),
    path('login/myquestions/', views.myquestions, name='myquestions'),

    path('contact/', views.contact, name='contact'),

    path('category/', views.show_category, name='category'),
]