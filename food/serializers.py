from rest_framework import serializers
from food.models import UserCalorie, Food
from django.contrib.auth.models import User
from rest_framework import permissions
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    food = serializers.PrimaryKeyRelatedField(many=True, queryset=Food.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'food')

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    #images  = serializers.PrimaryKeyRelatedField(many=True, queryset=Img.objects.all())
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

        
    class Meta:
        model = User
        fields = ('username','password')

class FoodSerializer(serializers.ModelSerializer):
    item = serializers.CharField(max_length=200)
    calories = serializers.IntegerField()

    class Meta:
        model = Food
        fields = ('id','item','calories')

class UserCalorieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    image = serializers.ImageField(max_length=None)

    class Meta:
        model = UserCalorie
        fields = ( 'id','image','owner')