from django.contrib import admin
from blog.models import Post, Category, Tag



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("picture","title","content","user","pub_date","updated_date",)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)