from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='image/girl.jpeg', upload_to='image/', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.user.username
    
class Mensajes(models.Model):
    
    user = models.ForeignKey(User, verbose_name="Mensajes", 
                             related_name='mensajes',
                             on_delete=models.CASCADE)
    content =  models.TextField()
    image_content = models.ImageField(upload_to='send/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    
    time_send = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['time_send']
    
    def __str__(self):
        return self.user.username