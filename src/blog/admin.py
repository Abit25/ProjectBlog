from django.contrib import admin
from .models import Post,Comment

# Register your models here.
@admin.register(Post)
class PostAdminChange(admin.ModelAdmin):
    list_display = ['title','slug','author','status']
    prepopulated_fields = { 'slug' : ('title',) }
    raw_id_fields = ('author',)

admin.site.register(Comment)
