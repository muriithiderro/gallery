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

class ModelsTest(TestCase):
    def setUp(self):
        self.category = Category(name="Books")
        self.location = Location(name="Nairobi")
        self.image = Image(name='git', description="wow image", category=self.category,location=self.location)

    def test_image_instantiation_is_proper(self):
        self.assertEquals(self.image.name, 'git')

    def test_location_instantiation_is_proper(self):
        self.assertEquals(self.location.name, 'Nairobi')
        
    def test_category_instantiation_is_proper(self):
        self.assertEquals(self.category.name, 'Books')
    
    def test_images_are_proprerly_saved(self):
        Image.create(self.image.name)
        self.assertTrue(len(Image.objects.count()>0))