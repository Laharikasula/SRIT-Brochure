from django.db import models

# Create your models here.
class eventclub(models.Model):
    cap=models.CharField(max_length=50)
    pic1=models.ImageField(upload_to='assets/images')
    pic2=models.ImageField(upload_to='assets/images')
    pic3=models.ImageField(upload_to='assets/images')
    pic4=models.ImageField(upload_to='assets/images')
    pic5=models.ImageField(upload_to='assets/images')
    #pic6=models.ImageField(upload_to='assets/images')
    def __str__(self):
        return self.cap