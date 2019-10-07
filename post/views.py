from django.shortcuts import render
from .models import Post 
from .serializer import PostSerializer #form과 동일하게, 만들어준 serializer를 가져오고
from rest_framework import viewsets #rest_framework 안에서 새롭게 사용할 viewsets를 가져옵니다. 

#cbv 기반이기 때문에 class기반으로 만들어줍니다. 
class PostViewSet(viewsets.ModelViewSet): #API상의 CRUD를 담당해주는 것
    queryset = Post.objects.all() #Post라는 모델 안의 모든 객체들을 변수에 담습니다. 
    serializer_class = PostSerializer