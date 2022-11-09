from django.urls import path
from . import views

urlpatterns = [
    path('', views.FavoriteList.as_view(), name='favorite_list'),
    path('add/', views.FavoriteAdd.as_view(), name='favorite_add'),
    path('delete/<int:pk>/', views.FavoriteDelete.as_view(), name='favorite_delete'),
    #path('update/<int:pk>/', views.CartUpdate.as_view(), name='cart_update'),
]
