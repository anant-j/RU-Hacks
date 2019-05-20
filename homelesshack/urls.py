from django.urls import path
from . import views

urlpatterns = [
        path('', views.index),
        path('verify', views.verify),
        path('sms', views.sms_reply),
        ]