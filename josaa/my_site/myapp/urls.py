from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns=[
    path("",views.kun_index,name="myapp"),
    path("services",views.services,name="services"),
    path("contact",views.contact,name="contact"),
    path("predictor",views.predictor,name="predictor"),
    path("info", views.info, name="info"),
    path("questions", views.questions, name="questions"),
    path("trends", views.trends, name="trends"),
]