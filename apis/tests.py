from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Post
class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(
            title="Django for APIs",
            author="William S. Vincent",
        )
    def test_api_listview(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.author)