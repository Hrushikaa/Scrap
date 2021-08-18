
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('index.html', views.home, name='Home'),
    path('twitter.html', views.twitter, name='twitter'),
    path('youtube.html', views.youtube, name='youtube'),
    path('crypto.html', views.crypto, name='crypto'),
    path('about.html', views.about, name='about'),
    path('feedback.html', views.feedback, name='feedback'),

]