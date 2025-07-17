from django.urls import path

from accounts.views import SignUpAPIView, LoginAPIView, LogOutAPIView

urlpatterns = [
    path("signup/", SignUpAPIView.as_view(), name="signup"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogOutAPIView.as_view(), name="logout"),
]