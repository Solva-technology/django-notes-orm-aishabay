from django.urls import path

from notes.views import (all_notes, all_users, category_notes, note_detail,
                         notes_home, profile_page)

app_name = "notes"

urlpatterns = [
    path("", all_notes, name="all_notes"),
    path("home/", notes_home, name="home"),
    path(
        "notes/category/<str:category>/", category_notes, name="category_notes"
    ),
    path("notes/<int:note_id>/", note_detail, name="note_detail"),
    path("users/<int:user_id>/", profile_page, name="profile"),
    path("users/", all_users, name="users"),
]
