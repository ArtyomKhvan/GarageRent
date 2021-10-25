from django.urls import path
from accounts import views as accounts_views

app_name = "accounts"

# urlpatterns = [
#     path("login/", accounts_views.LoginView.as_view(), name="login"),
#     path("logout/", accounts_views.LogoutView.as_view(), name="logout"),
#     path("create/", accounts_views.RegisterView.as_view(), name="register"),
#     path("<int:pk>/", accounts_views.UserDetailsView.as_view(), name="profile"),
#     path("users/list/", accounts_views.UserView.as_view(), name="user_list")
# ]
