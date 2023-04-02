from django.contrib import admin
from .models import BlogVideoFragment,BlogImageFragment,Blog,BlogComment

admin.site.register(BlogVideoFragment)
admin.site.register(BlogImageFragment)

admin.site.register(Blog)
admin.site.register(BlogComment)