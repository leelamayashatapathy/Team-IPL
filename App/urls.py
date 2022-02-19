
from unicodedata import name
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('detail/<str:id>', views.teamdetails, name="teamdetails"),
    path('detail/playerdetail/<str:id>', views.playerdetails, name="playerdetails"),
    path('updateplayer/',views.updateplayer,name="updateplayer"),
    path('updateteam/',views.updateteam,name="updateteam"),
    path('search/',views.search,name="search"),

]