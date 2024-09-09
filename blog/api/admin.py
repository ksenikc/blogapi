from django.contrib import admin
from .models import Post, Comment, Category

# Показ таблиц в панеле администратора
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
