from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Custom auth URLs pointing to our templates
    path('login/', 
         auth_views.LoginView.as_view(
             template_name='fees/login.html',
             redirect_authenticated_user=True
         ), 
         name='login'),
    
    path('logout/', 
         auth_views.LogoutView.as_view(next_page='home'), 
         name='logout'),
    
    path('register/', views.register, name='register'),
    path('download-clearance/', views.download_clearance, name='download_clearance'),
]