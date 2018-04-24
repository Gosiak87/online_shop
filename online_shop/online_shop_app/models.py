from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=160, db_index=True)
    slug = models.SlugField(max_length=160, db_index=True, unique=True)     # name without unacceptable characters in urls

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=160, db_index=True)
    slug = models.SlugField(max_length=160, db_index=True)
    image = models.ImageField(upload_to='images', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='products', null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)      # Index together to improve query performance to use these two fields, because we're dealing with images

