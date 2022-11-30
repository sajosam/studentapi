from django.shortcuts import render

# Create your views here.

from .serializers import TopicSerializer, CommentSerializer
from .models import tbl_comments,tbl_topics
from rest_framework import generics
# import mixins
from rest_framework import mixins

class TopicList(generics.ListCreateAPIView):
    queryset = tbl_topics.objects.all()
    serializer_class = TopicSerializer

class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tbl_topics.objects.all()
    serializer_class = TopicSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = tbl_comments.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = tbl_comments.objects.all()
    serializer_class = CommentSerializer

class individual_comments(generics.ListAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        topic_id = self.kwargs['topic_id']
        return tbl_comments.objects.filter(topic_id=topic_id)
