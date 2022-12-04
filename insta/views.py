from .models import Post 
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from rest_framework import generics


class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request, *args, **kwargs):
        # print 비추 logger 추천
        print("request.body: ", request.body)
        print("request.POST: ", request.POST)
        return super().dispatch(request, *args, **kwargs)
