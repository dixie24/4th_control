from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    

class Tasks(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title