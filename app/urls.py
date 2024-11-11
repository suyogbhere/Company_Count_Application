from django.urls import path
from app import  views
from allauth.account import views as auth_views 


urlpatterns=[
    path('', views.index, name='index'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html'),name='account_login'),   #LoginForm
    path('accounts/signup/',auth_views.SignupView.as_view(template_name='app/signup.html'),name='account_signup'),   #SignupForm
    path('accounts/logout/',auth_views.LogoutView.as_view(),name='account_logout'),

]
