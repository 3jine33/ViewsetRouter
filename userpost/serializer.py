from .models import UserPost 
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

		# author.username을 author_name으로 삼겠다.
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = UserPost
        fields = ['pk', 'author_name', 'title', 'body'] # 필드 값 변경