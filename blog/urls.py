from django.urls import path
from blog.views import index,add_post,edit_post,delete_post


app_name = "blog"


urlpatterns = [
    path('index/',index, name="index"),
    path('add-post/',add_post,name="add_post"),
    path('edit-post/<int:post_id>/',edit_post,name="edit_post"),
    path('delete-post/', delete_post, name="delete_post"),
]