from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='category_images')

    def __str__(self):
        return self.name

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)

        if img.width > 700 or img.height > 400:
            output_size = (700, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Channel(models.Model):
    title = models.CharField(max_length=200)
    channel_url = models.CharField(max_length=200)
    channel_username = models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='channel_images')
    description = models.TextField()
    subscribers = models.IntegerField()
    language = models.ForeignKey(Language, on_delete=set("Other"))
    category = models.ForeignKey(Category, on_delete=set("Other"))
    is_active = models.BooleanField(default="False")
    is_featured = models.BooleanField(default="False")
    # CAREFULL -> if user is deleted, their posts will be deleted as well
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.title

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
