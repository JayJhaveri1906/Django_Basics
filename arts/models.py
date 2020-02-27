from django.db import models
from datetime import datetime

# Create your models here.

class Arts(models.Model):
    title = models.CharField(max_length=100)
    
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d/")
    # this makes a photo folder with year month and day...folers inside it.^^
    #eg photos/2020/feb/28th
    #hence secure, as imgs are not stored in database.

    author = models.CharField(max_length=100)

    description = models.TextField()

    uploaded_at = models.DateTimeField(default = datetime.now,
    blank = True)

    def __str__(self):
        return self.title
    # We gave it a name for calling it.
    class Meta:
        verbose_name_plural = "Arts"
    
