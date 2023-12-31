from rest_framework import viewsets
from blog.api.serializers import PostSerializer
from blog.models import Post

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()