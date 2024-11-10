from django import forms
from .models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginDetails
        fields = ['username', 'password']


class UserForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['first_name', 'last_name', 'email_address', 'login_details']


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['description', 'status']


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'image', 'published']


class NotificationsForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = ['post', 'sender', 'receiver_id', 'is_seen']
