from django.urls import path
from webapp.views import general_view, car_view

app_name = "webapp"

urlpatterns = [
    path('', general_view.IndexView.as_view(), name="index"),
    path('about_us/', general_view.AboutUsView.as_view(), name="about_us"),
    path('cars/', car_view.CarListView.as_view(), name="car_list"),
    path('cars/<int:pk>/', car_view.CarDetailView.as_view(), name="car_detail"),
    path('contacts/', general_view.ContactView.as_view(), name="contacts")
]
