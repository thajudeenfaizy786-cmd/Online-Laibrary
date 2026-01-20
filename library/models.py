from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='profiles/',blank=True,null=True)
    phone=models.IntegerField(max_length=10,blank=True,null=True)
    bio=models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username

class Category(models.Model):
    cate=models.CharField(max_length=30)

    def __str__(self):
        return self.cate

class Collections(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=30)
    cate=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='books')
    image=models.ImageField(upload_to='collections',null=True,blank=True)

    def __str__(self):
        return self.title

class FavoriteBooks(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    book=models.ForeignKey(Collections,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}-{self.book}"