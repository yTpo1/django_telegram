from django.urls import path
from . import views
# authentication
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('check_your_email/', views.inform_activation_link, name='inform_activation'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
