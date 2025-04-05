from django.urls import path
from . import views
from django.http import HttpResponse
from .views import home
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', home, name='home'),  # Gyökérút hozzáadása
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Redirect to 'home' after logout
    path('profile', views.edit_profile, name='profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset_form'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]