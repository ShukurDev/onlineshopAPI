from django.db import models


# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=150, null=True)
    # icon = models.
    slug = models.SlugField(max_length=800)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    #updated = models.DateTimeField(auto_created=True)
    activate = models.BooleanField()

    def __str__(self):
        return self.name if self.name else super.__str__()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    title = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=4, verbose_name='price')
    photo = models.ImageField(upload_to='', null=True, blank=True)
    description = models.TextField()
    #color = models.ForeignKey(Color, models.SET_NULL)
    quality = models.IntegerField()
    #solid = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url


