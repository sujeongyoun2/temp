"""Ihelpr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import Ihelprapp.views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', Ihelprapp.views.home, name='home'),
    url(r'^home', Ihelprapp.views.home, name='home'),
    url(r'^about', Ihelprapp.views.about, name='about'),
    url(r'^application', Ihelprapp.views.application, name='application'),
    url(r'^forParents', Ihelprapp.views.forParents, name='forParents'),
    url(r'^forSitters', Ihelprapp.views.forSitters, name='forSitters'),
    url(r'^logIn', Ihelprapp.views.logIn, name='logIn'),
    url(r'^messages', Ihelprapp.views.messages, name='messages'),
    url(r'^messagesBox', Ihelprapp.views.messagesBox, name='messagesBox'),
    url(r'^myFavorite', Ihelprapp.views.myFavorite, name='myFavorite'),
    url(r'^myPage', Ihelprapp.views.myPage, name='myPage'),
    url(r'^myPosts', Ihelprapp.views.myPosts, name='myPosts'),
    url(r'^parents_signup', Ihelprapp.views.parents_signup, name='parents_signup'),
    url(r'^postPage', Ihelprapp.views.postPage, name='postPage'),
    url(r'^qna', Ihelprapp.views.qna, name='qna'),
    url(r'^signUp', Ihelprapp.views.signUp, name='signUp'),
    url(r'^sitters_signup', Ihelprapp.views.sitters_signup, name='sitters_signup'),
    url(r'^viewPost_forParents', Ihelprapp.views.viewPost_forParents,
        name='viewPost_forParents'),
    url(r'^viewPost', Ihelprapp.views.viewPost, name='viewPost'),
    url(r'^askQuestion', Ihelprapp.views.askQuestion, name='askQuestion'),
    url(r'^askCreated', Ihelprapp.views.askCreated, name='askCreated'),
    url(r'^postJobwant', Ihelprapp.views.postJobwant, name='postJobwant'),
    url(r'^postJobOpening', Ihelprapp.views.postJobOpening, name='postJobOpening'),
    url(r'^member_insert', Ihelprapp.views.member_insert, name='member_insert'),
    url(r'^member_login', Ihelprapp.views.member_login, name='member_login'),
    url(r'^log_out', Ihelprapp.views.log_out, name='log_out'),
    url(r'^postJob', Ihelprapp.views.postJob, name='postJob'),
    url(r'^search', Ihelprapp.views.search, name='search'),
    url(r'^viewPost_forParents', Ihelprapp.views.viewPost_forParents,
        name='viewPost_forParents'),
    url(r'^editMyPost', Ihelprapp.views.editMyPost, name='editMyPost'),
    url(r'^deleteMyPost', Ihelprapp.views.deleteMyPost, name='deleteMyPost'),

]
