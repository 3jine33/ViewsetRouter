from django.shortcuts import render
from .serializer import UserSerializer
from rest_framework import viewsets
from .models import UserPost
from rest_framework.filters import SearchFilter
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser


# Create your views here.
class UserPostViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    

    filter_backends = [SearchFilter] # 어떤 필터를 기반으로 필터링을 진행할 것인지 지정
    search_fields =('title', 'body') # 어떤 컬럼을 기반으로 검색을 진행할 것인지 지정, 쉼표 필수!


    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user) # 현재 로그인한 유저를 가져온다.
        # 로그인이 되어 있지 않다면 비어있는 쿼리셋을 리턴
        else:
            qs = qs.none()
        return qs

    # Create를 호출하는 함수
    def perform_create(self, serializer):
        serializer.save(author=self.request.user) # serializer를 save할 때 author에 현재 로그인한 유저 저