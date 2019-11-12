from django.contrib import admin
from blogging.models import Post, Category  # <-- import Category


admin.site.register(Post)
admin.site.register(Category)               # <-- Register Category
