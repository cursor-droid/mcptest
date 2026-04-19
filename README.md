# mcptest

Django-based demo clothing store (Jira **KAN-2**): catalog, cart, guest checkout, Stripe Checkout for card payments, owner analytics and order management, customer contact/chat, and favorites for logged-in users.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
# Add Stripe test keys from https://dashboard.stripe.com/test/apikeys
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser   # staff user for /owner/ and admin
python manage.py runserver
```

- Shop: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Owner dashboard: http://127.0.0.1:8000/owner/ (requires `is_staff`)

## Stripe

Payments use **Stripe Checkout** (hosted, PCI-friendly). Without keys in `.env`, checkout shows an error until you configure `STRIPE_SECRET_KEY` and `STRIPE_PUBLISHABLE_KEY`.

## Quality gates

```bash
black --check .
ruff check .
pytest -q
pre-commit install   # optional local hooks
```

## CI

GitHub Actions runs Black, Ruff, `manage.py migrate`, `manage.py check`, and pytest on pushes and pull requests to `main`.
