"""
URL configuration for ToDoList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from List import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.login, name="login"),
    path('forgot-password/', views.forgot_password, name="forgot_password"),
    path('register/', views.register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add-list-item/', views.add_list_item, name="add_list_item"),
    path('edit-status/<int:list_id>/', views.edit_status, name="edit_status"),
    path('delete-list-item/<int:list_id>/', views.delete_todo, name="delete_list_item"),
    path('search-name/', views.search_name, name="search_name"),
    path('logout/', views.logout, name="logout"),
    path('create-post/', views.posts, name="posts"),
    path('posts/', views.list_posts, name="list_posts"),
    path('edit-post/<int:post_id>/', views.edit_post, name="edit_post"),
    path('delete-post/<int:post_id>/', views.delete_post, name="delete_post"),
    path('my-posts/', views.my_posts, name="my_posts"),
    path('edit-list-item/<int:id>', views.edit_list_item, name="edit_list_item"),
    path('test_email/', views.test_email, name='test_email'),
    path('notification/', views.notification_count, name='notification'),
    path('user_details/', views.get_user_details, name='user_details')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
