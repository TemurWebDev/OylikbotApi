from django.urls import path
from .views import UserApiView,UserUpdateApiView,UserView,OylikUpdateApiView,SanaUpdateApiView,OylikView,SanaView,OylikViewUser

urlpatterns = [
    path('usertg/',UserApiView.as_view()),
    path('user/<str:user_id>/',UserView.as_view()),
    path('userupdate/<int:pk>/',UserUpdateApiView.as_view()),
    path('oylikal/',OylikView.as_view()),
    path('oylik/<str:user_id>/<str:oy>/',OylikViewUser.as_view()),
    path('sana/',SanaView.as_view()),
    path('oylikupdate/<int:pk>',OylikUpdateApiView.as_view()),
    path('sanaupdate/<int:pk>',SanaUpdateApiView.as_view())

]
