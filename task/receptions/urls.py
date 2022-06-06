from unicodedata import name
from django.urls import path
from .views import Home,receptionview,Addreception,deletereception,ingredienttop
from . import views

urlpatterns = [
   path('',Home.as_view(),name="home"),
   path('foodmaker/<int:pk>',receptionview.as_view(),name='foodmaker'),
   path('addnew/',Addreception,name='addnew'),
   path("foodmaker/<int:pk>/remove",deletereception.as_view(), name="delete"),
   path('foodmaker/rating/<int:reception_id>', views.submitrating, name='submitratings'),
   path("ingredient_top",views.ingredienttop, name="inggredienttopfive")
]