from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('topic/', views.TopicList.as_view(), name='topic-list'),  #list all topics
    path('topic/<int:pk>/', views.TopicDetail.as_view(), name='topic-detail'), #get a topic
    path('comment/', views.CommentList.as_view(), name='comment-list'), #list all comments
    path('comment/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'), #get a comment
    path('topic/<int:topic_id>/comments/', views.individual_comments.as_view(), name='individual-comments'), #get all comments for a topic

    path('get/topic/', views.gettopic.as_view(), name='get-topic'), #get all topics
    path('post/topic/', views.posttopic.as_view(), name='post-topic'), #post a topic

    path('get/comment/', views.getcomments.as_view(), name='get-comment'), #get all comments
    path('post/comment/', views.postcomments.as_view(), name='post-comment'), #post a comment

    path('get/topic/<int:pk>/', views.gettopicdetail.as_view(), name='get-topic-detail'), #get a topic
    path('get/comment/<int:pk>/', views.getcommentdetail.as_view(), name='get-comment-detail'), #get a comment

    path('post/topic/<int:pk>/', views.posttopicdetail.as_view(), name='post-topic-detail'), #post a topic
    path('post/comment/<int:pk>/', views.postcommentdetail.as_view(), name='post-comment-detail'), #post a comment

    path('get/topic/<int:pk>/comments/', views.gettopiccomments.as_view(), name='get-topic-comments'), #get all comments for a topic
    path('post/topic/<int:pk>/comments/', views.posttopiccomments.as_view(), name='post-topic-comments'), #post a comment for a topic

]
