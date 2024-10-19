from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, ArticleDetail


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, 
                         HomePageView)
    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_article_list_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_article_detail_url_resolves_view(self):
        url = reverse('news-detail', kwargs={
            'year': 2024,
            'month': 10,
            'day': 14,
            'slug': 'dedpul-i-rosomaha'
        })
        self.assertEqual(resolve(url).func.view_class, ArticleDetail)

