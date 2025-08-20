from django.urls import path
from . import views


urlpatterns = [
    path("", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("register/", views.RegisterView.as_view(), name="register"),


]