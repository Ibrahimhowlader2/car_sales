from django.urls import path
from . import views

urlpatterns = [
    path("signUp/", views.signUpView.as_view(), name="signUp"),
    path("logIn/", views.logInView.as_view(), name="logIn"),
    path("logOut/", views.logOutView.as_view(), name="logOut"),
    path("profile/", views.profileView.as_view(), name="profile"),
    path("edit_profile/", views.editProfileView.as_view(), name="edit_profile"),
    path("change_password/", views.changePasswordView.as_view(), name="change_password"),
    
    
]