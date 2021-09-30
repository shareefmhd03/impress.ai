from bot.views import home, login_view, logout_view, telegram_post, register
from django.urls import path

urlpatterns = [
    path('post/<str:data>',telegram_post, name="post"),
    path('',home, name="home"),
    path('login/',login_view, name="login_view"),
    path('register/',register, name="register"),
    path('logout/',logout_view, name="logout"),
]