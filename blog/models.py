from django.db import models


class BlogPost(models.Model):
    title = models.CharField()
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        BlogPost, related_name="comments", on_delete=models.CASCADE
    )
    author = models.CharField()
    content = models.TextField()

    def __str__(self):
        return f"{self.author} on {self.post.title}"
