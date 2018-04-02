from django.http import HttpResponse
from food.models import UserCalorie, Food
from food.serializers import UserCreateSerializer, UserCalorieSerializer, FoodSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
# from uusapp.serializers import UserSerializer, UserCreateSerializer
from rest_framework import permissions
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import permissions
# from food.permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# FOR TOKENS http://fdfdev.com/?p=946
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from django.template.loader import get_template

from food.deep_l import Deep
import numpy as np
import io, cv2

def index(request):
    return HttpResponse("Welcome to food caloire estimation")

class CreateUserView(generics.CreateAPIView):
    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserCreateSerializer

class UserList(generics.ListAPIView):
	# permission_classes = (permissions)
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class CaloireEstimate(generics.CreateAPIView):
    serializer_class = UserCalorieSerializer

    def create(self, request, *args, **kwargs):
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        img = cv2.imdecode(np.fromstring(request.data['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
        t = Deep(img)
        serializer1 = FoodSerializer(Food.objects.get(item=t))
        owner = self.request.user
        item = t
        calories = serializer1.data['calories']
        dat = UserCalorie(owner=owner, item=item, calories=calories)
        dat.save()
        serializer = UserCalorieSerializer(data=dat)
        if serializer.is_valid():
            serializer.save()
        return Response("Succesfully Uploaded")

class FoodCalorie(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer