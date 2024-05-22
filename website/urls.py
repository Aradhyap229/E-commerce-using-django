"""from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
path('', views.getData),
path('post/', views.postData),
]"""
from django.urls import path

from website.views import AuthenticatedRoute, CreateUser, Login
urlpatterns = [
    path('createUser', CreateUser.as_view(), name="create_user"),
    path('login', Login.as_view(), name='login'),
    path('test',AuthenticatedRoute.as_view(), name="tets")
]