from django.core.management.base import BaseCommand
from accounts.models import Users, Roles
from django.utils import timezone


class Command(BaseCommand):
    help = "Populate the Users table with initial data"

    def handle(self, *args, **kwargs):
        # Define some roles
        admin_role, created = Roles.objects.get_or_create(
            role_name="admin",
            defaults={"can_view": True, "can_edit": True, "can_delete": True},
        )
        editor_role = Roles.objects.get_or_create(
            role_name="editor",
            defaults={"can_view": True, "can_edit": True, "can_delete": False},
        )[0]
        viewer_role = Roles.objects.get_or_create(
            role_name="viewer",
            defaults={"can_view": True, "can_edit": False, "can_delete": False},
        )[0]

        # Create some users
        user1 = Users.objects.create_user(
            email="john@example.com",
            employee_id="E12345",
            firstname="John",
            lastname="Doe",
            contact_number="1234567890",
            date_created=timezone.now(),
            role=admin_role,
            password="password123",  # This will be hashed automatically
        )

        user2 = Users.objects.create_user(
            email="jane@example.com",
            employee_id="E67890",
            firstname="Jane",
            lastname="Smith",
            contact_number="0987654321",
            date_created=timezone.now(),
            role=editor_role,
            password="securepassword",  # This will be hashed automatically
        )

        self.stdout.write(self.style.SUCCESS("Users table populated successfully."))
