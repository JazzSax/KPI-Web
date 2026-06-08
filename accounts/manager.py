from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(
        self, email, employee_id, firstname, lastname, password=None, **extra_fields
    ):
        """
        Create and return a regular user with the given email, employee_id,  firstname, lastname, and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        if not employee_id:
            raise ValueError("The Employee ID field must be set")

        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)
        user = self.model(
            email=email,
            employee_id=employee_id,
            firstname=firstname,
            lastname=lastname,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, employee_id, firstname, lastname, password=None, **extra_fields
    ):
        """
        Create and return a superuser with the given email, employee_id,  firstname, lastname, and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            email, employee_id, firstname, lastname, password, **extra_fields
        )
