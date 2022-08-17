from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single/', views.single, name='single'),
    path('crypto-news/', views.crypto_news, name='crypto-news'),
    path('us-news/', views.us_news, name='us-news'),
    path('israel-news/', views.israel_news, name='israel-news'),
    path('article/<int:article_id>', views.article, name='article')
]
