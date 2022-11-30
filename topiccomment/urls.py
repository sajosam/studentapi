from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('topic/', views.TopicList.as_view(), name='topic-list'),
    path('topic/<int:pk>/', views.TopicDetail.as_view(), name='topic-detail'),
    path('comment/', views.CommentList.as_view(), name='comment-list'),
    path('comment/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path('topic/<int:topic_id>/comments/', views.individual_comments.as_view(), name='individual-comments'),
]
