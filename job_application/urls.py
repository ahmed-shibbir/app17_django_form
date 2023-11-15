from django.urls import path
from . import views   # . refers to current folder. it is possible because urls and views file are in the same directory

urlpatterns = [
    path('', views.index, name='index') # 3 arguments, # empty string '' relates to home page, otherwise a sub directory  like about etc should hsave been provided.

]