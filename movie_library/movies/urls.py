from re import M
from django.urls import path
from movies.api.veiwstes import MovieListCreateAPIView , MovieRetrieveUpdateDestroyAPIView

urlpatterns  = [
    path('movies-list' , MovieListCreateAPIView.as_view() , name= 'list'),
    path('<int:pk>' ,MovieRetrieveUpdateDestroyAPIView.as_view() , name= 'detail'),
]