from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.store,name="store"),
    path('cart/', views.cart,name="cart"),
    path('checkout', views.checkout,name="checkout"),
    ]
