from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    image = models.ImageField(default='default.jpg', upload_to='images')
    name = models.TextField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, help_text="(F)emale, (M)ale, (O)thers")
    phone = models.TextField(max_length=10)
    address = models.TextField(max_length=300)
    social_media = models.TextField(max_length=1000, help_text="Your social media link so we can know more about you")
    education = models.TextField(max_length=500, help_text="Details of your highest education")
    current_company = models.TextField(max_length=500, help_text="Where do you work")
    current_salary = models.TextField(max_length=500, help_text="Your current salary")
    about = models.TextField(max_length=500, help_text="Write about yourself")
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    