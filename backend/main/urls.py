from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about-us/', views.about_us, name='about_us'),
    path('ideathon/', views.ideathon, name='ideathon'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('idea-submission-form/', views.idea_submission_form, name='idea_submission_form'),
    path('ideathon/submit/', views.submit_idea, name='submit_idea'),
    path('contact/', views.contact, name='contact'),
    path('collaboration/', views.collaboration, name='collaboration'),
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
]
