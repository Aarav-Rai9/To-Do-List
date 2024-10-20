from django.db import models


# Create your models here.
class LoginDetails(models.Model):
    username = models.CharField(max_length=225)
    password = models.CharField(max_length=225)


class UserDetails(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email_address = models.EmailField(max_length=254)
    login_details = models.OneToOneField(LoginDetails, on_delete=models.CASCADE)


class ToDoList(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    user_details = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=1)


class Posts(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='posts/images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)
