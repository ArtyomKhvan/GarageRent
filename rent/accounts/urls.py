from django.urls import path
from accounts import views as accounts_views

app_name = "accounts"

urlpatterns = [
    path("login/", accounts_views.LoginView.as_view(), name="login"),
    path("logout/", accounts_views.LogoutView.as_view(), name="logout"),
    path("create/", accounts_views.RegisterView.as_view(), name="register"),
    path("<int:pk>/", accounts_views.UserDetailView.as_view(), name="profile"),
    path("profile/<int:pk>/edit", accounts_views.UserChangeView.as_view(), name="edit_profile"),
    path("profile/<int:pk>/change_password", accounts_views.ChangePasswordView.as_view(), name="change_password")
]
