from django.urls import path
from auth_app import views as AuthAppViews

app_name = "auth_app"

urlpatterns = [
    path("login/", AuthAppViews.LoginView.as_view(), name="login")
]