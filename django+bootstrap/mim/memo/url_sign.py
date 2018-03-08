from django.conf.urls import url
from django.contrib import admin
from memo import views

urlpatterns = [
url(r'^$',views.display_sign_html ),
url(r'^regNum/',views.regNum),
url(r'^register/', views.register),
]