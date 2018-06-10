from django.test import TestCase
from . models import Image,Category,Location
from .views import home
from django.urls import resolve
from django.core.urlresolvers import reverse

class HomeViewTest(TestCase):
    '''This test the home views ''' 
    def setUp(self):
     
        url = reverse('home')
        response = self.client.get(url)

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

#    self.category = Category(name="Books")
        # self.location = Location(name="Nairobi")
        # self.image = Image.objects.create(name='git', description="wow image", category=self.category,location=self.location)