from django.db import models


class Location(models.Model):
    PLACES = (
        ('Nairobi','Nairobi'),
        ('Mombasa','Mombasa'),
        ('Nyeri','Nyeri')
    )
    name = models.CharField(max_length=120, choices = PLACES)
  
    def create(self):
        pass
    def delete(self):
        pass
    def update(self):
        pass
    def search(self):
        pass

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
        pass
    def delete(self):
        pass
    def update(self):
        pass
    def search(self):
        pass

    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=120, unique=True, blank=False, null=False) 
    photo = models.ImageField(upload_to='uploads', null=False, blank=False)
    description = models.TextField()
    location = models.ForeignKey(Location, related_name='loc')
    category = models.ForeignKey(Category, related_name='cat')

    class Meta:
        pass

    def __str__(self):
        return self.name

    def create(self):
        pass
    def delete(self):
        pass
    def update(self):
        pass
    def get(self):
        pass
    def search(self):
        pass

