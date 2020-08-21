from django.urls import path
from third_app import views

app_name = 'app'

urlpatterns = [
    path('user_login/',views.user_login, name ='login'),
    path('register/', views.register,name='register'),
]