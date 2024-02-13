app_name = "accounts"


from django.urls import path
from .views import *



urlpatterns=[
    path("" , home , name="home") , 

    path("login/" , user_login ,            name="user-login") , 
    path("register/" , user_registration ,  name="user-register") , 
    path("logout/" , user_logout ,          name="user-logout") , 
    path("api/forget-pass/" , forget_pass_view ,name="forget-pass") , 
    path("api/sent-otp/" , sent_otp_api , name="sent_otp_api"),
    path("profile/" , profile , name="profile"),
    path("update-profile/" , update_profile , name="update-profile"),
]