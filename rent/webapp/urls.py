from django.urls import path
from webapp.views import general_view

app_name = "webapp"

urlpatterns = [
    path('', general_view.IndexView.as_view(), name="index"),
    path('about_us/', general_view.AboutUsView.as_view(), name="about_us")
]
