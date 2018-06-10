from django.db import models


class Location(models.Model):
    PLACES = (
        ('Nairobi','Nairobi'),
        ('Mombasa','Mombasa'),
        ('Nyeri','Nyeri')
    )
    name = models.CharField(max_length=120, choices = PLACES)
  
    def create(self):
        Location.objects.create(self)
    def delete(self):
        Location.objects.create(self)
    
    def search(self):
        loc = Location.filter(name=self.name)
        return loc

    class Meta:
        pass

    def __str__(self):
        return self.name

class Category(models.Model):
    CATEGORIES = (
        ('Cars','Cars'),
        ('Houses','Houses'),
        ('Books','Books')
    )
    name = models.CharField(max_length=120, choices =CATEGORIES)
    def create(self):
        Category.objects.create(self)
    def delete(self):
        Category.objects.create(self)
    
    def search(self):
        cat = Category.filter(name=self.name)
        return cat

    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=120, unique=True, blank=False, null=False) 
    photo = models.ImageField(upload_to='uploads', null=False, blank=False)
    description = models.TextField()
    location = models.ForeignKey(Location, related_name='loc',on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='cat',on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return self.name

    def create(self):
        Image.objects.create(self)
    def delete(self):
        Image.objects.create(self)
    
    def search(self):
        image = Image.filter(name=self.name)
        return image

