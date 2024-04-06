from rest_framework import serializers
from .models import TelegramUser,Oylik,Sana

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'

class SanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sana
        fields = '__all__'


class OylikSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Oylik
        fields = '__all__'






