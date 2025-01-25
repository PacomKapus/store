from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CreateProduct(models.Model):
    SECTION_CHOICES = [
        ('ALL', 'All Goods'),
        ('PAINTINGS', 'Paintings'),
        ('WALL_PANELS', 'Wall Panels'),
        ('FIGURES', 'Figures'),
        ('LETTERING', 'Lettering'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    photo = models.URLField(max_length=200)
    title = models.CharField(blank=True,null=True, max_length=50)
    text = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    section = models.CharField(max_length=20,choices=SECTION_CHOICES, default='ALL')
    likes = models.ManyToManyField(User,related_name='liked_comments')
    created_at = models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    title = models.CharField(max_length=50,null=True, blank=True)
    text = models.TextField()
    like = models.ManyToManyField(User, blank=True)
    
    def __str__(self):
        return self.title
    
    