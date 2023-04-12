from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ['id','username','first_name','last_name','email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    
    class Meta:
        model = Profile
        fields = "__all__"