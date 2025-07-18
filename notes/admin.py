from django.contrib import admin

from notes.models import Category, Note, Status, User, UserProfile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    search_fields = ["title", "description"]
    list_filter = ["title"]


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["text", "author", "status", "created_at"]
    search_fields = ["text"]
    list_filter = ["status"]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["name", "is_final"]
    search_fields = ["name"]
    list_filter = ["is_final"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    search_fields = ["name", "email"]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["bio", "birth_date", "user"]
    search_fields = ["bio", "user"]
