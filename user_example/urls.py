from django.urls import path, include
from . import views

urlpatterns = [
    path('sentiment/', views.sentiment, name="sentiment"),
    path('classification/', views.classification, name="classification"),
    path('concepts/', views.concepts, name="concepts"),
    path('entities/', views.entities, name="entities"),
    path('summary/', views.summary, name="summary"),
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
]
