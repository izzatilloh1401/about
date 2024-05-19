from django.contrib import admin
from .models import Post, Comments, Tag

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass