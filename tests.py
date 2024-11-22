from django.test import TestCase, Client
from django.urls import reverse
from .models import Post
from .views import blog_views
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_project.settings")
django.setup()  # Подключаем настройки Django

class BlogViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post_1 = Post.objects.create(title="First Post", content="This is the first post")
        cls.post_2 = Post.objects.create(title="Second Post", content="This is the second post")

    def setUp(self):
        self.client = Client()

    def test_blog_view_returns_all_posts(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post_1.title)
        self.assertContains(response, self.post_2.title)

    def test_blog_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'blogapp/blog_page.html')



