from rest_framework import generics
from core.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser, DjangoModelPermissions

# giving permision to the owner of the post to only the author of the post .
class PosrUserWritePermision(BasePermission):
    message = "Editing post is restricted to the author only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author ==request.user

class PostList(generics.ListCreateAPIView):
    permision_classes = [DjangoModelPermissions]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer



class PostDetails(generics.RetrieveUpdateDestroyAPIView, PosrUserWritePermision):
    permision_classes = [PosrUserWritePermision]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
