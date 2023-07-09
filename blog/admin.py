from django.contrib import admin
from . import models

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Post)
class Authoradmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "name", "email", "publish", "status")
    list_filter = ("status", "publish")
    search_fields = ("name", "email", "content")

admin.site.register(models.Category)    


# Register your models here.
# ID: luiscarbogniani pass: probando123
