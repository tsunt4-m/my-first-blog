from django.contrib import admin
from .models import Post

"""
Adminページ（管理画面）での動作などを記述。

"""

# Register your models here.
admin.site.register(Post)