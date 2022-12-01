from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.posts , name="posts"),
    path('post/<int:id>' , views.post , name="post"),
    path("add/", views.AddPost.as_view(), name="add"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("update/<int:pk>", views.PostUpdate.as_view(), name="update"),
] 
