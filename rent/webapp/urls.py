from django.urls import path
from webapp.views import general_view

app_name = "webapp"

urlpatterns = [
    path('', general_view.IndexView.as_view(), name="index"),
    path('about_us/', general_view.AboutUsView.as_view(), name="about_us"),
    path('cars/', general_view.CarListView.as_view(), name="car_list"),
    path('cars/<int:pk>/', general_view.CarDetailView.as_view(), name="car_detail")
]
