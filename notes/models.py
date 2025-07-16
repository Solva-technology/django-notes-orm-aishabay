from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UserProfile(models.Model):
    bio = models.TextField(verbose_name="Биография")
    birth_date = models.DateField(verbose_name="Дата рождения")
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="userprofile",
        verbose_name="Пользователь",
    )

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"


class Status(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name="Статус")
    is_final = models.BooleanField(default=False, verbose_name="Окончательный")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Note(models.Model):
    text = models.TextField(verbose_name="Текст")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Статус")
    categories = models.ManyToManyField(Category, verbose_name="Категории")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"
