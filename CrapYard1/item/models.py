from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta: 
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name 
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    condition = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.name     

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 600,600


        if self.image:
            image = Image.open(self.image.path)
            image.thumbnail(SIZE, Image.LANCZOS)
            image.save(self.image.path)







   
    def __str__(self):
        return self.name 