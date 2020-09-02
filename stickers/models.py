from django.db import models
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Sticker(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to="sticker_images")
    sticker_url = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=set("Other"))

    def __str__(self):
        return self.title

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

