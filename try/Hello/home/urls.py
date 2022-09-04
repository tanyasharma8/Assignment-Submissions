from django.contrib import admin
from django.urls import path,include
from home import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path("", views.index, name='home'),
    path("shop",views.shop,name='shop'),
    path("about", views.about, name='about'),
    path("blog", views.blog, name='blog'),
    path("cart", views.cart, name='cart'),
    path("login",views.loginUser,name="login"),
    # path("password_change/",auth_views.PasswordChangeView.as_view(),name='password_change'),
    # path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path("change_password",views.change_password,name="change_password")
    # path("contact", views.contact, name='contact')


]
