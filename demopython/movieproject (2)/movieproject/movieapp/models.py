from django.db import models


# Create your models here.
class Movie(models.Model):

    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)


    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'


    def  get_url(self):
            return reverse('movieapp:movie_by_category',args=[self.slug])
    def __str__(self):
            return  '{}'.format(self.name)



class Viewusr(models.Model):
    pass

class Deleteusr(models.Model):
    pass


