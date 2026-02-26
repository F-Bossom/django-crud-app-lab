from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.CardList.as_view(), name='card-index'),
    path('cards/create', views.CardCreate.as_view(), name='card-create'),
    path('cards/<int:pk>', views.card_detail, name='card-detail'),
    path('cards/<int:card_id>/add-condition/', views.add_condition, name='add_condition'),
    path('cards/<int:card_id>/associate-tag/<int:tag_id>', views.associate_tag, name='associate-tag'),
    path('cards/<int:pk>/update', views.CardUpdate.as_view(), name='card-update'),
    path('cards/<int:pk>/delete', views.CardDelete.as_view(), name='card-delete'),
    path('tags/create', views.TagCreate.as_view(), name='tag_create'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tag_detail'),
    path('tags/<int:pk>/update', views.TagUpdate.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete', views.TagDelete.as_view(), name='tag-delete'),
    path('tags/', views.TagList.as_view(), name='tag_list'),
]