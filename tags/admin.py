from django.contrib import admin
from .models import Tag, CatTag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(CatTag)
class CatTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat', 'tag')