from django.contrib import admin
from .models import Blog, Comment, Reply

admin.site.site_header = "D&C Blog Admin"
admin.site.site_title = "D&C Blog Admin Area"
admin.site.site_header = "Welcome To D&C Blog Admin Area"

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Reply)
