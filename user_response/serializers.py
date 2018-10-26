from rest_framework import serializers
from .models import User,Saver


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name","req_no","lat", "lng","no_of_person","no_of_severe_person","timestamp","pickup")

class SaverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saver
        fields = ("name","lat","lng","is_free","next_destination","saver_no")
