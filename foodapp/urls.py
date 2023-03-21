

from django.urls import path
from .views import *

urlpatterns = [
    path('', indexView, name="indexView"),
    path('signup', signupView, name="signup"),
    path('login', loginView, name="login"),
    path('logout', logoutView, name="logout"),
    path('profile', profileView, name="profile"),
    path('food/detail/<int:id>/',foodDetail,name="foodDetail"),
    path('add-to-cart', addToCart, name="addToCart"),
    path('cart', cartView, name="cart"),
    path('update-cart', updateCartView, name="updateCart"),
    path('delete-cart', deleteCartView, name="deleteCart"),
    path('checkout', checkoutView, name="checkout"),
    path('place-an-order', placeanOrderView, name="placeanorder"),
]
