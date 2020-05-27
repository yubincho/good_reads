from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=60, unique=True)

    def __str__(self):
        if self.username == None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return str(self.username)

    # def __str__(self):
    #    return str(self.username)

    class Meta:
        verbose_name_plural = "User"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="", upload_to="profile_pictures")
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = " User Profile"


class AllLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ": " + str(self.date)
