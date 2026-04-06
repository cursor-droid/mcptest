from decimal import Decimal

from django.core.management.base import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    help = "Create sample clothing products for local development."

    def handle(self, *args, **options):
        samples = [
            {
                "name": "Classic Cotton Tee",
                "slug": "classic-cotton-tee",
                "description": "Soft everyday tee.",
                "price": Decimal("24.99"),
                "quality": Product.Quality.GOOD,
                "stock": 50,
            },
            {
                "name": "Slim Denim Jeans",
                "slug": "slim-denim-jeans",
                "description": "Stretch denim with a slim fit.",
                "price": Decimal("79.00"),
                "quality": Product.Quality.PREMIUM,
                "stock": 30,
            },
            {
                "name": "Wool Winter Coat",
                "slug": "wool-winter-coat",
                "description": "Warm wool blend coat.",
                "price": Decimal("199.00"),
                "quality": Product.Quality.LUXURY,
                "stock": 12,
            },
        ]
        for row in samples:
            obj, created = Product.objects.update_or_create(
                slug=row["slug"],
                defaults={
                    "name": row["name"],
                    "description": row["description"],
                    "price": row["price"],
                    "quality": row["quality"],
                    "stock": row["stock"],
                    "is_active": True,
                },
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"{'Created' if created else 'Updated'} {obj.name}",
                ),
            )
