from django.shortcuts import get_object_or_404, render

from notes.models import Note, User, UserProfile


def notes_home(request):
    return render(request, "notes/notes_home.html")


def all_notes(request):
    notes = (
        Note.objects.select_related("author", "status")
        .prefetch_related("categories")
        .all()
    )
    return render(request, "notes/all_notes.html", context={"notes": notes})


def category_notes(request, category):
    notes = (
        Note.objects.filter(categories__title=category)
        .select_related("author", "status")
        .prefetch_related("categories")
        .all()
    )
    context = {"category": category, "notes": notes}
    return render(request, "notes/all_notes_by_category.html", context)


def note_detail(request, note_id):
    note = get_object_or_404(
        Note.objects.select_related(
            "author", "status", "author__userprofile"
        ).prefetch_related("categories"),
        id=note_id,
    )
    return render(request, "notes/note_detail.html", context={"note": note})


def profile_page(request, user_id):
    user_profile = get_object_or_404(
        UserProfile.objects.select_related("user"), id=user_id
    )
    notes = Note.objects.filter(author__id=user_id).select_related("status").all()
    context = {"user_profile": user_profile, "notes": notes}
    return render(request, "notes/profile_page.html", context)


def all_users(request):
    users = User.objects.all()
    return render(request, "notes/users.html", context={"users": users})
