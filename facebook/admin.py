from django.contrib import admin
from facebook.models import Comment
from facebook.models import Article

admin.site.register(Article)
admin.site.register(Comment)