from django.urls import path
from webapp.views import general_view

app_name = "webapp"

urlpatterns = [
    path('', general_view.IndexView.as_view(), name="index"),
]
