from .models import Post 
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)

# public_post_list = PublicPostListAPIView.as_view()

@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def perform_create(self, serializer):
    #     author = self.request.user
    #     ip = self.request.META['REMOTE_ADDR']
    #     serializer.save(author=author, ip=ip)

    # def dispatch(self, request, *args, **kwargs):
    #     # print 비추 logger 추천
    #     print("request.body: ", request.body)
    #     print("request.POST: ", request.POST)
    #     return super().dispatch(request, *args, **kwargs)
