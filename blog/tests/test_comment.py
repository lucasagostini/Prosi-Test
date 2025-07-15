from pytest import fixture, mark
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog.models import BlogPost, Comment


@fixture
def api_client():
    return APIClient()


@mark.django_db
def test_create_comment_success(api_client):
    """POST /posts/{id}/comments/ creates a new comment"""
    post = BlogPost.objects.create(title="Foo", content="Bar")
    url = reverse(
        "post-comments", args=[post.id]
    )  # adjust name if your nested route differs
    data = {"author": "Alice", "content": "Nice post!"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["author"] == data["author"]
    assert response.data["content"] == data["content"]
    assert response.data["post"] == post.id


@mark.django_db
def test_create_comment_invalid(api_client):
    """POST /posts/{id}/comments/ with missing data returns 400"""
    post = BlogPost.objects.create(title="Foo", content="Bar")
    url = reverse("post-comments", args=[post.id])
    data = {"author": "", "content": ""}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "author" in response.data
    assert "content" in response.data


@mark.django_db
def test_create_comment_post_not_found(api_client):
    """POST /posts/{id}/comments/ for nonexistent post returns 404"""
    url = reverse("post-comments", args=[999])
    data = {"author": "Alice", "content": "Hello"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@mark.django_db
def test_list_comments_not_allowed(api_client):
    """GET /posts/{id}/comments/ is not allowed (or returns list if implemented)"""
    post = BlogPost.objects.create(title="Foo", content="Bar")
    url = reverse("post-comments", args=[post.id])
    response = api_client.get(url)
    # either list is not supported or returns list
    assert response.status_code in (
        status.HTTP_405_METHOD_NOT_ALLOWED,
        status.HTTP_200_OK,
    )
