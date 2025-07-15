from rest_framework import serializers
from .models import BlogPost, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "content"]


class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    comments_count = serializers.IntegerField(source="comments.count")

    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "comment_count", "comments"]
