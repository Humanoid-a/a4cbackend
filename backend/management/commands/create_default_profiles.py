# backend/management/commands/create_default_profiles.py

from django.core.management.base import BaseCommand
from django.db import transaction
from backend.models import FrontendUser, UserProfile

class Command(BaseCommand):
    help = "Create a default UserProfile for every FrontendUser missing one."

    def handle(self, *args, **options):
        users = FrontendUser.objects.filter(profile__isnull=True)
        total = users.count()
        if not total:
            self.stdout.write(self.style.SUCCESS("All users already have profiles."))
            return

        self.stdout.write(f"Found {total} users without a profile. Creating defaults…")
        created = 0

        with transaction.atomic():
            for user in users:
                # create with your chosen defaults
                UserProfile.objects.create(
                    user=user,
                    sat_reading=200,
                    sat_math=200,
                    gpa=0.00,
                    recommendation_strength=1,
                    nationality='',  # or your preferred “blank” country
                    # intended_major and gender use their model defaults
                )
                created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {created} profiles."))
