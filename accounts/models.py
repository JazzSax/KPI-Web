from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    Group,
    Permission,
)
from .manager import CustomUserManager


class Roles(models.Model):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("editor", "Editor"),
        ("viewer", "Viewer"),
        # Add more roles as needed
    ]

    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)
    can_view = models.BooleanField(default=True)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    otm_dlv = models.BooleanField(default=False)
    eqp_util = models.BooleanField(default=False)
    cst_cmp = models.BooleanField(default=False)
    exc = models.BooleanField(default=False)
    cst_rst = models.BooleanField(default=False)
    ops_b1f1_ass_yld = models.BooleanField(default=False)
    sft = models.BooleanField(default=False)
    cost = models.BooleanField(default=False)

    def __str__(self):
        return self.role_name


class Users(AbstractBaseUser, PermissionsMixin):
    account_id = models.AutoField(primary_key=True)
    employee_id = models.CharField(_("employee id"), unique=True, max_length=50)
    email = models.EmailField(_("email address"), unique=True, null=False)
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    contact_number = models.CharField(max_length=12, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    role = models.ForeignKey(
        Roles, on_delete=models.SET_NULL, null=True, related_name="users"
    )

    is_staff = models.BooleanField(default=False)  # determines admin access
    is_active = models.BooleanField(
        default=True
    )  # Can disable account without deleting

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["employee_id", "firstname", "lastname"]

    def save(self, *args, **kwargs):
        # Check if the password is already hashed
        if self.pk and not self.password.startswith("pbkdf2_"):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
