from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ArtPiece(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey('Category')

    def __str__(self):
        return '{} ({})'.format(self.name, self.category)
