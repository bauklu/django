from django.urls import path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('update/', authapp.update, name='update'), 
    path('verify/<str:email>/<str:activation_key>/', authapp.verify, name='verify'),

]
