from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.

class Keywords(models.Model):
    tag = models.CharField(max_length=50, unique=True, verbose_name='Tags')
    
    class Meta():
        db_table = 'keywords'

    def __str__(self):
        return self.tag 


class Album(models.Model):
    album_name = models.CharField(max_length=200, blank=True)
    albums_img = models.ImageField(upload_to='albums', blank=True)
    keywords = models.ManyToManyField(Keywords, related_name='albums', related_query_name='album', verbose_name='keywords')
    
    class Meta():
        db_table = 'album'

    def __str__(self):
        return self.album_name
    

class Photo(models.Model):
    name = models.CharField(max_length=200, blank=True)
    file = models.ImageField(upload_to="images/%Y/%m/%d")
    album = models.ForeignKey(Album, related_name='photos', related_query_name='photo')
    location = models.CharField(blank=True, max_length=200)

    class Meta():
        db_table = 'photo'


    