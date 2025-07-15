from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import BlogPost
from .serializers import BlogPostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    @action(detail=True, methods=["post"], url_path="comments", url_name="comments")
    def create_comment(self, request, pk: None):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def post_list_page(request):
    return render(request, "blog/post_list.html")


def post_detail_page(request, pk):
    # ensures 404 if invalid ID, but we only need pk in the template
    get_object_or_404(BlogPost, pk=pk)
    return render(request, "blog/post_detail.html", {"post_id": pk})
