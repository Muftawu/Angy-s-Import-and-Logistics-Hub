from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid 

from .utils import * 

class User(AbstractUser):
    first_name = models.CharField(max_length=MAX_STR_LEN, null=True, blank=True)
    last_name = models.CharField(max_length=MAX_STR_LEN, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = uuid.uuid4()
            super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name()


class Product(models.Model):
    name = models.CharField(max_length=MAX_STR_LEN, null=True, blank=True)
    price = models.IntegerField()
    quantity = models.CharField(max_length=MAX_DIGIT_LEN, choices=[(i,i) for i in range(0, MAX_QUANTITY_LEN)])
    tracking_number = models.CharField(max_length=MIN_STR_LEN, unique=True, null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = uuid.uuid4()
            super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.tracking_number}"

class Batch(models.Model):
    batch_number = models.CharField(max_length=MAX_DIGIT_LEN, choices=[(i,i) for i in range(0, MAX_QUANTITY_LEN)])
    logistics_used = models.CharField(max_length=MAX_STR_LEN, choices=[(logts, logts) for logts in LOGISTICS_COMPANY])
    amount_received = models.IntegerField()
    all_good_received = models.BooleanField(default=False)
    batch_experience = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = uuid.uuid4()
            super(Batch, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.batch_number} - {self.logistics_used}"