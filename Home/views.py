from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from  .CustumPermition import CreatorOrReadonly
from rest_framework.mixins import ListModelMixin
from Profile.models import Profile
from Profile.serializer import ProfileSerializer
from .models import (Blog,
                     BlogComment,
                     BlogVideoFragment,
                     BlogImageFragment,
                    )
from .serializer import (BlogSerializer,BlogCommentSerializer,
                         BlogVideoFragmentSerializer)

from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BlogViewset(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,CreatorOrReadonly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['author','gener','date']
    search_fields = ['title','images__text','videos__text']
    OrderingFilter = ['date',"likes"]


class BlogCommentViewset(ModelViewSet):
    serializer_class = BlogCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,CreatorOrReadonly]

    def get_queryset(self):
        blog_id = self.kwargs['blog_pk']
        blog = Blog.objects.get(id = blog_id)
        return BlogComment.objects.filter(blog = blog)
    
class ProfileViewset(ReadOnlyModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,CreatorOrReadonly]


    def get_queryset(self):
        blog_id = self.kwargs['blog_pk']
        blog = Blog.objects.get(id = blog_id)
        profile = Profile.objects.filter(user = blog.author)
        
        return profile
     
        

            
            
              
    
    


    


