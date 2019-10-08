from django.shortcuts import render
from .models import Post 
from .serializer import PostSerializer 
from rest_framework import viewsets 
from .pagination import MyPagination

# 클래스 추가
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    pagination_class = MyPagination # 추가