from django.db import models
from hr.models import Department, Designation
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from tenant.models import Tenant, TenantAwareModel

roles = [
    ('admin', 'Admin'),
    ('clerk', 'Clerk'),
    ('accountant', 'Accountant'),
    ('driver', 'Driver'),
]


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, blank=False)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, choices=roles, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, null=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("user-detail", kwargs={"pk": self.pk})
