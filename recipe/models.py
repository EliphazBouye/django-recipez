
from django.db import models


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    description = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.recipe_name


class Image(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image')
