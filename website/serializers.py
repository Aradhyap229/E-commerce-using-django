from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    title= serializers.CharField(label="Enter Product Name")
    id=serializers.IntegerField(label="Enter Product Id")
    campany=serializers.CharField(label="Enter  campany")



class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


    