from django.contrib import admin

from notes.models import Category, Note, Status, User, UserProfile


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    search_fields = ["title", "description"]
    list_filter = ["title"]


class NoteAdmin(admin.ModelAdmin):
    list_display = ["text", "author", "status", "created_at"]
    search_fields = ["text"]
    list_filter = ["status"]


class StatusAdmin(admin.ModelAdmin):
    list_display = ["name", "is_final"]
    search_fields = ["name"]
    list_filter = ["is_final"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    search_fields = ["name", "email"]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["bio", "birth_date", "user"]
    search_fields = ["bio", "user"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
