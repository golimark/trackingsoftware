from django.urls import path
from auth_app import views as AuthAppViews

app_name = "auth_app"

urlpatterns = [
    path("login/", AuthAppViews.login_view, name="login"),
    path("logout/", AuthAppViews.logout_view, name="logout")
]