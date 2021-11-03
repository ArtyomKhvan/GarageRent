from django.urls import path
from webapp.views import general_view, car_view

app_name = "webapp"

urlpatterns = [
    path('', general_view.IndexView.as_view(), name="index"),
    path('about_us/', general_view.AboutUsView.as_view(), name="about_us"),
    path('cars/', car_view.CarListView.as_view(), name="car_list"),
    path('cars/<int:pk>/', car_view.CarDetailView.as_view(), name="car_detail"),
    path('contacts/', general_view.ContactView.as_view(), name="contacts"),
    path('cars/<int:pk>/review/create/', car_view.ReviewCreateView.as_view(), name="review_create"),
    path('cars/new/', car_view.CarCreateView.as_view(), name="car_create"),
    path('cars/<int:pk>/delete/', car_view.CarDeleteView.as_view(), name="car_delete"),
    path('cars/<int:pk>/photo/new/', car_view.PhotoCreateView.as_view(), name="photo_create")
]
