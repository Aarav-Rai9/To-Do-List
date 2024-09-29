from django.http import HttpResponse
from logging import exception
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
import json
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if form.is_valid():
            if LoginDetails.objects.filter(username__icontains=username, password__icontains=password):
                login = LoginDetails.objects.get(username=username, password=password)
                user_details = UserDetails.objects.get(login_details=login)
                full_name = user_details.first_name + " " + user_details.last_name
                request.session['full_name'] = full_name
                request.session['user_id'] = user_details.id
                return redirect("dashboard")
            return render(request, "login.html", {"error": "Username or Password are Incorrect"})
    return render(request, "login.html")


def forgot_password(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        email_address = request.POST.get("email_address")

        if form.is_valid():
            pass
    return render(request, "forgot-password.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_address = request.POST.get('email_address')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')

        if password == repeat_password:
            username = ""
            for char in email_address:
                if char == "@":
                    break
                username += char

            login = LoginDetails.objects.create(username=username, password=password)
            user = UserDetails.objects.create(first_name=first_name, last_name=last_name, email_address=email_address,
                                              login_details=login)
            return redirect("login")
        return render(request, "register.html", {"error": "Passwords Do Not Match"})

    else:
        return render(request, "register.html", {"error": ""})


def dashboard(request):
    user = UserDetails.objects.get(id=request.session.get("user_id", None))
    list = ToDoList.objects.filter(user_details=user)
    #for i in list:
    #list = ToDoList.objects.all()
    #print(request.session.get("user_id", None))
    if request.method == "POST":
        status = request.POST.get("status")
        date = request.POST.get("created_at")
        user_details = UserDetails.objects.filter(user_id__icontains=request.session.user_id)

        if date == "" and status == "":
            list = ToDoList.objects.all()
        elif date != "" and status != "":
            list = ToDoList.objects.filter(status__icontains=status, created_at__icontains=date)
        elif date == "":
            list = ToDoList.objects.filter(status__icontains=status)
        else:
            list = ToDoList.objects.filter(created_at__icontains=date)
    return render(request, "index.html", {"list": list})


def search_name(request):
    if request.method == "POST":
        name = request.POST.get("search_name")
        if name != "":
            list = ToDoList.objects.filter(description__icontains=name)
        else:
            list = ToDoList.objects.all()
        return render(request, "index.html", {"list": list})


def add_list_item(request):
    if request.method == "POST":
        form = ToDoListForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("dashboard")


def edit_status(request, list_id):
    list = get_object_or_404(ToDoList, id=list_id)
    if request.method == "POST":
        form = ToDoListForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    return render(request, "edit_status.html", {"list": list})


def delete_todo(request, list_id):
    list = get_object_or_404(ToDoList, id=list_id)
    list.delete()
    return redirect("dashboard")


def logout(request):
    request.session.flush()
    return redirect("login")


def posts(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        user_id = request.session.get("user_id", None)
        user_detail = get_object_or_404(UserDetails, id=user_id)
        if form.is_valid():
            content = form.save()
            content.author = user_detail
            content.save()
            return redirect("list_posts")
    return render(request, "Posts.html")


def list_posts(request):
    posts = Posts.objects.filter(published__icontains=1)
    return render(request, "list_posts.html", {"posts": posts, "user_id": request.session.get("user_id", None)})


def edit_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("my_posts")
    return render(request, "edit_post.html", {"post": post})


def delete_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    post.delete()
    return redirect("list_posts")


def my_posts(request):
    user_id = request.session.get("user_id", None)
    user_detail = get_object_or_404(UserDetails, id=user_id)
    posts = Posts.objects.filter(author=user_detail)
    return render(request, "my_posts.html", {"posts": posts})


def edit_list_item(request, id):
    obj = get_object_or_404(ToDoList, id=id)
    # obj.title = request.POST.get("description")
    description = json.loads(request.body)
    obj.description = description['description']
    try:
        obj.save()
    except exception as e:
        print(e)
    print(obj)
    data = {"id": obj.id, "description": obj.description, "created_at": obj.created_at, "status": obj.status}
    return JsonResponse(data)


def test_email(request):
    subject = 'test subject'
    body = 'test'
    recipient_list = ['anuradhaah667@gmail.com', 'dummy95252749@gmail.com']
    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, recipient_list)
    return HttpResponse("email sent.")

#def send_http_email(request):