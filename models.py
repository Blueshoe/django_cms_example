from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=64)
	slug = models.CharField(max_length=64)

class ArtPiece(models.Model):
	name = models.CharField(max_length=64)
	image = models.ImageField(blank=True, null=True)
	category = models.ForeignKey('Category')
