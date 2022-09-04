"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "E-Commerce Admin"
admin.site.site_title = "E-Commerce Admin Portal"
admin.site.index_title = "Welcome to E-Commerce Researcher Portal"

urlpatterns = [
    path('admin/',admin.site.urls),
    path("", views.index, name='home'),
    path("shop",views.shop,name='shop'),
    path("about", views.about, name='about'),
    path("cart", views.cart, name='cart'),
    path("contact", views.contact, name='contact'),
    path("blog", views.blog, name='blog'),
    path("login", views.loginUser, name='login'),
    path("change_password",views.change_password,name='change_password')


]
