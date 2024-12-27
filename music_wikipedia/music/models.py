from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название группы")
    description = models.TextField(verbose_name="Описание группы")
    creation_date = models.DateField(verbose_name="Дата создания группы")
    image = models.ImageField(upload_to="groups", verbose_name="Изображение группы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Album(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название альбома")
    description = models.TextField(verbose_name="Описание альбома")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="albums", verbose_name="Группа")
    release_date = models.DateField(verbose_name="Дата выпуска альбома")
    cover_image = models.ImageField(upload_to="albums", verbose_name="Обложка альбома")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"


class Song(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название песни")
    description = models.TextField(blank=True, null=True, verbose_name="Описание песни")
    album = models.ForeignKey(
        Album, on_delete=models.SET_NULL, null=True, blank=True, related_name="songs", verbose_name="Альбом"
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, null=True, blank=True, related_name="songs", verbose_name="Группа"
    )
    duration = models.DurationField(verbose_name="Длительность песни")
    audio_file = models.FileField(upload_to="songs", verbose_name="Аудиофайл")
    lyrics = models.TextField(verbose_name="Текст песни")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"


class GroupMember(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя участника")
    biography = models.TextField(verbose_name="Биография участника")
    role = models.CharField(max_length=100, verbose_name="Роль в группе")
    birth_date = models.DateField(verbose_name="Дата рождения")
    photo = models.ImageField(upload_to="members", verbose_name="Фотография участника")
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="members", verbose_name="Группа"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Участник группы"
        verbose_name_plural = "Участники группы"
