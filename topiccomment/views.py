
from .models import tbl_topics, tbl_comments
from .serializers import TopicSerializer, CommentSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework import viewsets
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



class gettopic(APIView):
    def get(self, request, format=None):
        topic = tbl_topics.objects.all()
        serializer = TopicSerializer(topic, many=True)
        return Response(serializer.data)

class posttopic(APIView):
    def post(self, request, format=None):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class getcomments(APIView):
    def get(self, request, format=None):
        comments = tbl_comments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class postcomments(APIView):
    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class gettopicdetail(APIView):
    def get(self, request, pk, format=None):
        topic = tbl_topics.objects.get(pk=pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

class getcommentdetail(APIView):
    def get(self, request, pk, format=None):
        comment = tbl_comments.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

class posttopicdetail(APIView):
    def post(self, request, pk, format=None):
        topic = tbl_topics.objects.get(pk=pk)
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class postcommentdetail(APIView):
    def post(self, request, pk, format=None):
        comment = tbl_comments.objects.get(pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class gettopiccomments(APIView):
    def get(self, request, pk, format=None):
        comments = tbl_comments.objects.filter(topic_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class posttopiccomments(APIView):
    def post(self, request, pk, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)