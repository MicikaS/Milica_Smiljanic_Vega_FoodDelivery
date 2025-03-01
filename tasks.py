from invoke import task


@task
def build_local(c):
    """Builds the local environment with Docker Compose"""
    c.run("sudo docker-compose down --volumes --remove-orphans", pty=True)
    c.run("sudo docker-compose build --no-cache", pty=True)
    c.run("sudo docker-compose up -d", pty=True)


@task
def populate_db(c):
    """Populate the database with initial data."""
    print("🔄 Applying migrations...")
    c.run("sudo docker-compose exec web python manage.py migrate", pty=True)

    print("🔄 Creating superuser...")
    c.run(
        'sudo docker-compose exec web python manage.py shell -c """'
        "from django.contrib.auth import get_user_model\n"
        "User = get_user_model()\n"
        "if not User.objects.filter(username='milica').exists():\n"
        "    User.objects.create_superuser('milica', 'milica@example.com', 'milica')\n"
        "    print('✔️ Superuser created.')\n"
        "else:\n"
        "    print('Superuser already exists.')\n"
        '"""',
        pty=True,
    )

    print("🔄 Creating sample restaurants, food, couriers, and orders...")
    c.run(
        'sudo docker-compose exec web python manage.py shell -c """'
        "from restaurant.models import Restaurant, Food\n"
        "from order.models import Courier, Order\n"
        "from django.contrib.auth import get_user_model\n"
        "from django.utils.timezone import now\n"
        "from datetime import timedelta\n\n"
        "User = get_user_model()\n\n"
        "# Delete previous data\n"
        "Restaurant.objects.all().delete()\n"
        "Food.objects.all().delete()\n"
        "Courier.objects.all().delete()\n"
        "Order.objects.all().delete()\n\n"
        "# Create new restaurants\n"
        "r1 = Restaurant.objects.create(name='Pizza Place', location='Downtown')\n"
        "r2 = Restaurant.objects.create(name='Sushi Spot', location='Midtown')\n"
        "print('✔️ Restaurants created.')\n\n"
        "# Create food items\n"
        "f1 = Food.objects.create(name='Margherita Pizza', price=12.99, restaurant=r1)\n"
        "f2 = Food.objects.create(name='Spicy Tuna Roll', price=10.99, restaurant=r2)\n"
        "print('✔️ Food items created.')\n\n"
        "# Create couriers (Each restaurant has one courier)\n"
        "c1 = Courier.objects.create(name='John Doe', restaurant=r1)\n"
        "c2 = Courier.objects.create(name='Jane Smith', restaurant=r2)\n"
        "print('✔️ Couriers created.')\n\n"
        "# Assign orders\n"
        "user = User.objects.filter(username='milica').first()\n"
        "if user:\n"
        "    order1 = Order(user=user, restaurant=r1, status='pending', courier=c1, order_time=now())\n"
        "    order1.save()\n"
        "    order1.food.set([f1])\n"
        "    \n"
        "    order2 = Order(user=user, restaurant=r2, status='pending', courier=c2, order_time=now())\n"
        "    order2.save()\n"
        "    order2.food.set([f2])\n"
        "    \n"
        "    print('✔️ Sample orders created.')\n\n"
        '"""',
        pty=True,
    )

    print("✅ Database populated successfully!")


@task
def format(c):
    """Formats code using Black"""
    c.run("black .", pty=True)


@task
def test(c):
    """Runs Django tests"""
    c.run("sudo docker-compose exec web python manage.py test", pty=True)


@task
def makemigrations(c):
    """Runs makemigrations in Django"""
    c.run("sudo docker-compose exec web python manage.py makemigrations", pty=True)


@task
def migrate(c):
    """Runs database migrations"""
    c.run("sudo docker-compose exec web python manage.py migrate", pty=True)


@task
def createsuperuser(c):
    """Creates a superuser for Django Admin"""
    c.run("sudo docker-compose exec web python manage.py createsuperuser", pty=True)
