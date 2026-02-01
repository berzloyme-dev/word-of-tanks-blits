from django.db import models
from django.utils import timezone


class Nation(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class TankClass(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Tank(models.Model):
    TIER_CHOICES = [(i, f" {i}") for i in range(1, 11)]

    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)

    nation = models.ForeignKey('Nation', on_delete=models.CASCADE, related_name="tanks")
    tank_class = models.ForeignKey('TankClass', on_delete=models.CASCADE, related_name="tanks")
    tier = models.IntegerField(choices=TIER_CHOICES)

    image = models.ImageField(upload_to="tanks/", blank=True, null=True)

    hp = models.PositiveIntegerField(default=0)
    damage = models.PositiveIntegerField(default=0)
    penetration = models.PositiveIntegerField(default=0)
    armor = models.PositiveIntegerField(default=0)
    speed = models.PositiveIntegerField(default=0)

    is_premium = models.BooleanField(default=False)

    # MUHIM: auto_now_add YO‘Q
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} (T{self.tier})"


