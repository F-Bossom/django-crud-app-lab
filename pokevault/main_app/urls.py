from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.CardList.as_view(), name='card-index'),
    path('cards/create', views.CardCreate.as_view(), name='card-create'),
    path('cards/<int:pk>', views.CardDetail.as_view(), name='card-detail'),
    path('cards/<int:pk>/update', views.CardUpdate.as_view(), name='card-update'),
    path('cards/<int:pk>/delete', views.CardDelete.as_view(), name='card-delete'),
]