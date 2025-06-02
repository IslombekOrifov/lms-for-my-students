from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    phone = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    middle_name = models.CharField(max_length=223, null=True, blank=True)
    email = models.EmailField()

    photo = models.ImageField(upload_to="account/profile_pics/", blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    # role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.SET_NULL) # worker
    custom_uuid = models.UUIDField(unique=True, editable=False, null=True)
    father_phone = models.CharField(max_length=15, blank=True, null=True)
    mother_phone = models.CharField(max_length=15, blank=True, null=True)
    father_telegram_id = models.CharField(max_length=100, blank=True, null=True)
    mother_telegram_id = models.CharField(max_length=100, blank=True, null=True)
    
    start_work = models.DateField(blank=True, null=True)    # worker
    
    is_worker = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone}"