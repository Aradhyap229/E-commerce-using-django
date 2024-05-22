
"""from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .views import ProductView, VerifyAccountView, LoginView

from .serializers import ProductSerializer, VerifyAccountSerializer, LoginSerializer
from .models import Product
from django.http import HttpResponse
from .models import *
from .serializers import*




class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
           
            title = serializer.validated_data.get('title')
            product_id = serializer.validated_data.get('id')
            company = serializer.validated_data.get('company')
            
            Product.objects.create(title=title, id=product_id, company=company)
            
            return Response({'message': 'Product created successfully'}, status=201)
        else:
            
            return Response(serializer.errors, status=400)
        
        
        
class VerifyAccountView(APIView):
    def post(self, request):
        serializer = VerifyAccountSerializer(data=request.data)
        if serializer.is_valid():
            
            email = serializer.validated_data.get('email')
            otp = serializer.validated_data.get('otp')
           
            
            return Response({'message': 'Account verified successfully'}, status=200)
        else:
            
            return Response(serializer.errors, status=400)
        
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            
            
            return Response({'message': 'Login successful'}, status=200)
        else:
            
            return Response(serializer.errors, status=400)"""



"""class LoginAPI(APIView):
    def post(self ,request):
        try:
            data = request.data
            serializers = LoginSerializer(data = data)
            if serializers.is_valid():
                email = serializers.data['email']
                password = serializers.data[ 'password' ]
                return Response({
                    'status' : 400,
                    'message' : 'ki re ki haal chal',
                    'data' : serializers.errors
                })"""
"""def obtain_jwt_token(user):
    refresh = RefreshToken.for_user(user)
    token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return token"""


"""class ProductApiView(APIView):
    serializers_class=ProductSerializer
    def get(self,request):
        allProduct = Product.objects.all().values()
        return Response({"Message":"List of product","product List":allProduct})
    
    def post(self,request):
        print('Request data is : ',request.data)
        serializers_obj=ProductSerializer(data=request.data)
        if(serializers_obj.is_valid()):
            data=serializers_obj.validated_data
            productObj=Product.objects.create(id=data.get("id"),
                               title=data.get("title"),
                               campany=data.get("campany"))
            print("Hello",productObj)

        product = Product.objects.all().filter(id=request.data["id"]).values()
        return Response({"hello"})
"from rest_framework_simplejwt.tokens import RefreshToken

def obtain_jwt_token(user):
    refresh = RefreshToken.for_user(user)
    token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return token"""
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
#from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken


class CreateUser(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        username= request.data['username']
        email=request.data['email']
        password= request.data['password']
        user_obj=User.objects.create(username=username, email=email)
        user_obj.set_password(password)
        print(user_obj.id)
        return Response({"message":"user Created successfully"})

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class Login(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        username= request.data['username']
        password= request.data['password']
        user = authenticate(username=username, password=password)
        user=User.objects.get(username=username)
        token=get_tokens_for_user(user)
        return Response(token)


class AuthenticatedRoute(APIView):
    def get(self, request):
        print(request.user)
        return Response("hello")