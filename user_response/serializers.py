from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name","req_no","lat", "lng","no_of_person","no_of_severe_person","timestamp")
