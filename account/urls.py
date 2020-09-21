
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('addcourse/',views.AddCourse,name = 'addcourse'),
    path('extraadd/',views.extraadd,name = 'extraadd'),
    path('Content/<id>/',views.Content,name = 'content'),
    path('contentdetails/<id>/',views.Contentdetails,name = 'contentdetails'),
    path('increase/',views.increase,name='increase'),
    path('dashboard/',views.dashboard, name = 'dashboard'),
    path('StatusChange/',views.StatusChange,name = 'StatusChange'),
    path('contact/',views.contact,name = 'contact'),
    path('profile/',views.profile,name = 'profile'),
    
]

