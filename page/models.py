from django.db import models


# Create your models here.

class FoodPage(models.Model):
    infoname = models.CharField(blank=True, max_length=256)
    info = models.TextField(blank=False)
    img = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.infoname
