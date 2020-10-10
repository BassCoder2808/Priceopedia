from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login-page'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout-page'),
    path('register/',views.register,name='registeration-page'),
    path('search/',views.search,name='search-page'),
    path('profile/',views.profile,name='profile-page'),
    path('',views.home,name='home-page')
]
