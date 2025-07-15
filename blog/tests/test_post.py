import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog.models import BlogPost, Comment

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_list_posts_empty(api_client):
    """GET /posts/ returns an empty list when no posts exist"""
    url = reverse('post-list')  # adjust if your router basename differs
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == []

@pytest.mark.django_db
def test_create_post_success(api_client):
    """POST /posts/ with valid data creates a new post"""
    url = reverse('post-list')
    data = {'title': 'Test Post', 'content': 'This is a test.'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in response.data
    assert response.data['title'] == data['title']
    assert response.data['content'] == data['content']
    assert response.data.get('comment_count') == 0

@pytest.mark.django_db
def test_create_post_invalid(api_client):
    """POST /posts/ with missing fields returns 400"""
    url = reverse('post-list')
    data = {'title': '', 'content': ''}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'title' in response.data
    assert 'content' in response.data

@pytest.mark.django_db
def test_retrieve_post_with_comments(api_client):
    """GET /posts/{id}/ returns post detail with nested comments"""
    post = BlogPost.objects.create(title='Foo', content='Bar')
    Comment.objects.create(post=post, author='Alice', content='First comment')
    Comment.objects.create(post=post, author='Bob', content='Second comment')
    url = reverse('post-detail', args=[post.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == post.id
    assert response.data['title'] == post.title
    assert response.data.get('comment_count') == 2
    assert len(response.data.get('comments', [])) == 2
    authors = {c['author'] for c in response.data['comments']}
    assert authors == {'Alice', 'Bob'}

@pytest.mark.django_db
def test_retrieve_post_not_found(api_client):
    """GET /posts/{id}/ with invalid id returns 404"""
    url = reverse('post-detail', args=[999])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND