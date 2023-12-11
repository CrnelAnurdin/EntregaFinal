from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WatchList(models.Model):    
    name= models.CharField(max_length=50, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=100,default='')
    description = models.TextField(null=True,default='',blank=True)   
    date= models.DateTimeField(null=True,auto_now_add=True)
    rate = models.CharField(max_length=1,default='',blank=True)
    visto = models.BooleanField(default=False)
    category = models.CharField(max_length=50,default='',blank=True)
    
    def __str__(self):
        return self.title + ' - ' + self.user.username
    


    
class NewComentarios(models.Model):    
    name= models.CharField(max_length=50, blank=False)    
    email= models.CharField(max_length=100)
    telefono = models.CharField(max_length=15,null=True,blank=True)   
    mensaje= models.TextField(null=False,default='')        

    def __str__(self):
        return self.name + ' - ' + self.mensaje
    

    
