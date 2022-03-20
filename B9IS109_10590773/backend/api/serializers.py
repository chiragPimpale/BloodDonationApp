from dataclasses import field
from enum import unique
from pyexpat import model
from statistics import mode
from rest_framework import serializers
from api.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import string
import random
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

"""
user serializer to serlize all user data as JSON
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


"""
SingupSerializer is created for accepting data as JSON
"""
class SignupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=255, required=True)
    date_of_birth = serializers.DateField(required=False)
    user_type = serializers.CharField(max_length=50, required=True)
    blood_group = serializers.CharField(max_length=20, required=False)
    full_name = serializers.CharField(max_length=50, required=True)
    city = serializers.CharField(max_length=50, required=False)
    address = serializers.CharField(max_length=200, required=False)
    country = serializers.CharField(max_length=100, required=False)
    contact = serializers.CharField(max_length=20, required=False)
    gender = serializers.CharField(max_length=20, required=False)
    password = serializers.CharField(max_length=50, required=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use")
        return value
    
    def validate_contact(self, value):
        if User.objects.filter(contact=value).exists():
            raise serializers.ValidationError("Contact already in use")
        return value

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return User.objects.create(**validated_data)


"""
DonerSerializer is created to response data as JSON
"""
class DonerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "date_of_birth", "user_type", "blood_group", "full_name", "city", "address", "country", "contact", "gender"]
    


"""
Blood request serializer is created to get connected with donor id and acceptor id as JSON
"""
class BllodRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    blood_requested_by = serializers.CharField(required=True)
    blood_requested_to = serializers.CharField(required=True)

    def create(self, validated_data):
        user1 = User.objects.get(id=validated_data["blood_requested_by"])
        user2 = User.objects.get(id=validated_data["blood_requested_to"])
        return BloodRequest.objects.create(blood_requested_by=user1, blood_requested_to=user2)


"""
BllodRequestCheckSerializer is bllod bank account module wihcj will pass toke as JSON and get validated data as response 
"""
class BllodRequestCheckSerializer(serializers.ModelSerializer):
    blood_requested_by = UserSerializer(read_only=True)
    class Meta:
        model = BloodRequest
        fields = "__all__"



"""
BloodBankRequestSerializer is a bllod accepter module part to POST data as JSON
"""
class BloodBankRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    requested_by = serializers.CharField(required=True)
    requested_group = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.get(id=validated_data["requested_by"])
        validated_data["secret_key"] = self.get_random_string(50).upper()
        return RequestToBloodBankModel.objects.create(
            requested_by = user,
            secret_key = validated_data["secret_key"],
            requested_group = validated_data["requested_group"]
        )
    
    def get_random_string(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str



"""
VerifySecretTokeSerializer is created to post data as JSON for verify token
"""
class VerifySecretTokeSerializer(serializers.ModelSerializer):
    secret_key = serializers.CharField(required=True)
    requested_by = UserSerializer(read_only=True)
    requested_group = serializers.CharField(read_only=True)

    class Meta:
        model = RequestToBloodBankModel
        fields = "__all__"




"""
MyTokenObtainPairSerializer is a inherted serializer to create JWT token and response as JSON
"""
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        self.get_token(self.user)
        data["user"] = str(self.user)
        data["id"] = self.user.id
        data["full_name"] = str(self.user.full_name)
        data["user_type"] = str(self.user.user_type)
        return data


"""
AllTokenSerializer is created for retrive all token form from database as JSON
"""
class AllTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestToBloodBankModel
        fields = "__all__"
