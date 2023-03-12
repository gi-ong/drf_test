from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer

from insta.permissions import IsAuthorOrReadOnly
from .models import Post 
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action


# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)

# public_post_list = PublicPostListAPIView.as_view()



# @api_view(['GET'])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = []
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['message']

    def perform_create(self, serializer):
        # FIXME: 인증이 되어있다는 가정하에, author를 지정해보겠음.
        author = self.request.user # User or AnonymousUser
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(author=author, ip=ip)

    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public']) # public field만 업데이트
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'insta/post_detail.html'
    
    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({
            'post': PostSerializer(post).data,
        })



    # def perform_create(self, serializer):
    #     author = self.request.user
    #     ip = self.request.META['REMOTE_ADDR']
    #     serializer.save(author=author, ip=ip)

    # def dispatch(self, request, *args, **kwargs):
    #     # print 비추 logger 추천
    #     print("request.body: ", request.body)
    #     print("request.POST: ", request.POST)
    #     return super().dispatch(request, *args, **kwargs)
