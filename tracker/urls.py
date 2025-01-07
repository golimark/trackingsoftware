from django.urls import path
from tracker import views as TrackerViews

app_name = "tracker"

urlpatterns = [
    path("", TrackerViews.HomeView.as_view(), name="home")
]