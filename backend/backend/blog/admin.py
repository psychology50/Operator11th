from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_id', 'owner', 'create_dt', 'update_dt', )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_id', 'status', 'slug', 'author', 'create_dt', 'update_dt')
    prepopulated_fields = {'slug' : ('title',),}
    
    def tag_list(self, obj):
        return ','.join([t.name for t in obj.tags.all()])

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name', 'description')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'post', 'short_content', 'create_dt', 'update_dt')
