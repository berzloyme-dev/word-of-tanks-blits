from django.contrib import admin
from .models import Nation, TankClass, Tank


@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


@admin.register(TankClass)
class TankClassAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


@admin.register(Tank)
class TankAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tier", "nation", "tank_class", "hp")
    list_filter = ("tier", "nation", "tank_class")
    search_fields = ("name", "slug", "nation__name", "tank_class__name")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("-tier", "name")
