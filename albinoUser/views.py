from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import TelegramUser,Oylik,Sana
from .serializers import UserSerializer,OylikSerializer,SanaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



class UserApiView(ListCreateAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(RetrieveUpdateDestroyAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = UserSerializer



class UserView(APIView):
    def get(self, request, user_id):
        try:
            user = TelegramUser.objects.get(user_id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except:
            return Response(status.HTTP_201_CREATED)

    def put(self, request, user_id,format=None):
        user = TelegramUser.objects.get(user_id=user_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OylikView(ListCreateAPIView):
    queryset = Oylik.objects.all()
    serializer_class = OylikSerializer



class OylikViewUser(APIView):
    def get(self, request, user_id, oy):
        try:
            oylik = Oylik.objects.get(user__user_id=user_id,sana__name=oy)
            
            serializer = OylikSerializer(oylik)
            return Response(serializer.data)
        except:
            return Response(status.HTTP_201_CREATED)




class OylikUpdateApiView(RetrieveUpdateDestroyAPIView):
    queryset = Oylik.objects.all()
    serializer_class = OylikSerializer



class SanaView(ListCreateAPIView):
    queryset = Sana.objects.all()
    serializer_class = SanaSerializer



class SanaUpdateApiView(RetrieveUpdateDestroyAPIView):
    queryset = Sana.objects.all()
    serializer_class = SanaSerializer

