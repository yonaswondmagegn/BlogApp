from django.shortcuts import render
from .models import Profile
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from Home.CustumPermition import CreatorOrReadonly
from .serializer import ProfileSerializer
from Home.models import Blog
from Home.serializer import BlogSerializer



class ProfileViewset(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    permission_classes = [IsAuthenticatedOrReadOnly,CreatorOrReadonly]



class BlogViewset(ModelViewSet):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,CreatorOrReadonly]


    def get_queryset(self):
        profile_id = self.kwargs['profile_pk']
        profile = Profile.objects.get(id = profile_id)
        return Blog.objects.filter(author = profile.user)

