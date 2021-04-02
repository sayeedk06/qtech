from django.db import models

# Create your models here.
class Alluser(models.Model):
    username = models.CharField(max_length=100)
    userFirstname = models.CharField(max_length=100)
    userLastname = models.CharField(max_length=100)

    def __str__(self):
        return self.username



class SearchModel(models.Model):
    keywords = models.CharField(max_length=20)
    details = models.CharField(max_length=100)
    search_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Alluser,default=1,on_delete=models.CASCADE)

    def __str__(self):
        return self.keywords

class SearchTimeModel(models.Model):
    date = models.OneToOneField(SearchModel,on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.time