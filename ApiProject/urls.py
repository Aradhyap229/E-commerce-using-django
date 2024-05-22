"""
URL configuration for ApiProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
"""from django.contrib import admin
from django.urls import path
from django.urls  import  include

from website.views import ProductApiView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("product/",ProductApiView.as_view())
]   
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import obtain_jwt_token

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    if user is not None:
        token = obtain_jwt_token(user)
        return Response(token)
    else:
        return Response({'error': 'Invalid credentials'}, status=400)"""
"""from django.urls import path
from .views import ProductView, VerifyAccountView, LoginView

urlpatterns = [
    path('products/', ProductView.as_view(), name='product-list'),
    path('verify-account/', VerifyAccountView.as_view(), name='verify-account'),
    path('login/', LoginView.as_view(), name='login'),
]"""

from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('website.urls'))
]

