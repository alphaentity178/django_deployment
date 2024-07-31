from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserInfo(models.Model) :

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')

    facebook_id = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to="profile_pics" , blank=True)


    def __str__(self) :
        from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserInfo(models.Model) :

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')

    facebook_id = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to="profile_pics" , blank=True)


    def __str__(self) :
        return self.user.username