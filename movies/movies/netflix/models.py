from django.db import models
 
# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=50),

class movie(models.Model):
    title = models.CharField(max_length=100),
    overview = models.TextField(max_length=500),
    year = models.DateField(),
    poster = models.ImageField(upload_to="movies/posters"),
    video = models.FileField(upload_to="movies/video"),
    categories= models.ManyToManyField(category)
    country= models.ForeignKey(Country,null=True,on_delete=models.SET_NULL)
    rate= models.OneToOneField(Rate,null=True,on_delete=models.SET_NULL)
class Country(models.Model):
    name=models.CharField(max_length=233)

    def __str__(self):
        return str(self.title)

class Rate(models.Model):
    rate=models.IntegerChoices(null=True , blank=True)


    def __str__(self):
        return str(self.rate)