from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Categories(models.Model):
    cat_title = models.CharField(max_length=200, unique=True)
    cat_featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_on']
        verbose_name = "Categories"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.cat_title}"

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=200, default='Choose from this dropdown list')
    featured_image = CloudinaryField('image', default='placeholder')
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                     related_name="submitted_by")
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        # return reverse('post_detail', args=(str(self.pk)))
        return reverse('index')


