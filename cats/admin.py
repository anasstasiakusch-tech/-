from django.contrib import admin
from .models import Cat, Achievement, AchievementCat
from tags.models import CatTag  # импорт, но НЕ регистрация


class AchievementInline(admin.TabularInline):
    model = AchievementCat
    extra = 1


class CatTagInline(admin.TabularInline):
    model = CatTag
    extra = 1


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'birth_year', 'owner')
    inlines = [AchievementInline, CatTagInline]


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    