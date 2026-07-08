from django.contrib import admin
from .models import BlogCategory , Post , Comment


admin.site.register(BlogCategory)
admin.site.register(Post)
admin.site.register(Comment)
