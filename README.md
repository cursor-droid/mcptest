# mcptest

Django-based demo clothing store (Jira **KAN-2**): catalog, cart, guest checkout, Stripe Checkout for card payments, owner analytics and order management, customer contact/chat, and favorites for logged-in users.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```

See the repository for full documentation.
