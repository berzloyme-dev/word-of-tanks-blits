from itertools import count
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True, blank=True, db_index=True)
    intro = models.TextField()
    cover = models.ImageField(upload_to='articles/covers/')
    read_time = models.DurationField(blank=True, null=True)
    published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    important = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title, allow_unicode=True)
            base_slug = slug

            count = 1
            while Article.objects.filter(slug=base_slug).exists():
                base_slug = f"{slug}-{count}"
                count += 1

            self.slug = base_slug

        if self.important:
            Article.objects.exclude(pk=self.pk).filter(important=True).update(important=False)

        super().save(*args, **kwargs)


class Context(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='articles/contexts/', blank=True, null=True)

    def __str__(self):
        return self.article.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Moment(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='moments/')
    author = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def clean(self):
        if not self.phone_number and not self.email:
            raise ValidationError("telefon raqam yoki emaildan kamida bittasini kiriting.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
