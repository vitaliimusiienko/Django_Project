from django.db import models

class Notes(models.Model):
    title = models.CharField('title', max_length=50)
    text = models.CharField('text', max_length=250)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Note'
    

# Create your models here.
