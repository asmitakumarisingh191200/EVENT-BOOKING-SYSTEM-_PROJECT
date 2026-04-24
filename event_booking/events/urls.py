from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),       # direct '/' → signup page
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='events/login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('events/', views.event_list, name='event_list'),
    path('book/<int:event_id>/', views.book_event, name='book_event'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('weather/<int:event_id>/', views.weather_preview, name='weather_preview'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]