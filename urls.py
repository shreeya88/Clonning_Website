from django.contrib import admin
from django.urls import path
from myapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Index'),
    path('about',views.about, name='About'),
    path('contact', views.contact, name='contact'),
    path('cart',views.cart, name='cart'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('logoutUser',views.logoutUser, name='logoutUser'),
    path('SignUpUser', views.SignUpUser, name='SignUpUser')
]