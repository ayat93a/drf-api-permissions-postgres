from re import M
from django.urls import path
from movies.api.veiwstes import MovieListCreateAPIView , MovieRetrieveUpdateDestroyAPIView
from rest_framework_simplejwt import views as jwt_view

urlpatterns  = [
    path('movies-list' , MovieListCreateAPIView.as_view() , name= 'list'),
    path('<int:pk>' ,MovieRetrieveUpdateDestroyAPIView.as_view() , name= 'detail'),
    path('token' , jwt_view.TokenObtainPairView.as_view() , name = 'token_obtain'),
    path('refresh' , jwt_view.TokenRefreshView.as_view() , name = 'refresh'),
]



# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDAyMTYwOCwiaWF0IjoxNjUzOTM1MjA4LCJqdGkiOiJiZTM0MWYyZWFiNmU0NzA2OWZjZDFmNzU5MzRmNTFkNCIsInVzZXJfaWQiOjF9.5DSuPQ2NLVZWyCYtoi83XnT6TY6kV2NqXw6TGWTyFMc",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzOTM1NTA4LCJpYXQiOjE2NTM5MzUyMDgsImp0aSI6ImNiZWM2YzFiMzBlYTQ5YTViOTMyOWQ3Y2MxMGIzNjY5IiwidXNlcl9pZCI6MX0.r6kR3PCv2ZWuzdQ_OyB5MYjYdDi0BJXSz60fbFXZwkY"
# }