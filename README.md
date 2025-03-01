# Milica_Smiljanic_Vega_FoodDelivery
🍽️ Food Delivery API
A RESTful API for an online food delivery system, allowing users to order food, manage restaurants, and track orders.

📌 Features
✅ User Authentication (JWT-based login, registration, and roles)
✅ Restaurant Management (CRUD operations for restaurants)
✅ Food Menu Management (Add, update, delete, and list food items)
✅ Order Processing (Users can place orders, track status, and get estimated delivery times)
✅ Courier Assignment (Each restaurant has a dedicated courier for deliveries)
✅ Token-Based Security (JWT authentication required for most endpoints)

🚀 Tech Stack
Backend: Django & Django REST Framework (DRF)
Authentication: JWT (JSON Web Token)
Database: PostgreSQL (or SQLite for local testing)
Containerization: Docker (optional)
📌 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/MicikaS/Milica_Smiljanic_Vega_FoodDelivery.git
cd FoodDeliveryAPI
2️⃣ Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Apply Database Migrations
python manage.py migrate

5️⃣ Create a Superuser (Admin)
python manage.py createsuperuser
💡 Follow the prompts to set a username and password.

6️⃣ Run the Development Server
python manage.py runserver

✅ The API is now available at http://127.0.0.1:8000/api/

📌 API Endpoints
Endpoint	Method	Description	Authentication Required?
User Management			
/api/user/register/	POST	Register a new user	❌ No
/api/user/login/	POST	Obtain JWT token	❌ No
/api/user/password-reset/	POST	Reset password	❌ No
/api/user/list/	GET	List all users (admin only)	✅ Yes (Admin)
Restaurant Management			
/api/restaurant/	GET	List all restaurants	❌ No
/api/restaurant/	POST	Add a new restaurant (Admin only)	✅ Yes (Admin)
/api/restaurant/{id}/	GET	Retrieve a specific restaurant	❌ No
/api/restaurant/{id}/	PUT	Update restaurant details (Admin only)	✅ Yes (Admin)
/api/restaurant/{id}/	DELETE	Delete a restaurant (Admin only)	✅ Yes (Admin)
Food Menu Management			
/api/restaurant/menu/	GET	List all food items	❌ No
/api/restaurant/menu/	POST	Add a new food item (Admin only)	✅ Yes (Admin)
/api/restaurant/menu/{id}/	GET	Retrieve food item details	❌ No
/api/restaurant/menu/{id}/	PUT	Update food details (Admin only)	✅ Yes (Admin)
/api/restaurant/menu/{id}/	DELETE	Delete a food item (Admin only)	✅ Yes (Admin)
Order Management			
/api/order/	GET	List all orders (Admin only)	✅ Yes (Admin)
/api/order/	POST	Place an order	✅ Yes (User)
/api/order/{id}/	GET	Retrieve a specific order	✅ Yes (User/Admin)
📌 Authentication & Token Usage
1️⃣ Login and Get JWT Token

curl -X POST "http://127.0.0.1:8000/api/user/login/" \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "password"}'
✅ Response:
{
    "refresh": "YOUR_REFRESH_TOKEN",
    "access": "YOUR_ACCESS_TOKEN"
}

2️⃣ Use the Token in API Requests
Example: Get all restaurants
curl -X GET "http://127.0.0.1:8000/api/restaurant/" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
3️⃣ Refresh Expired Token

curl -X POST "http://127.0.0.1:8000/api/user/token/refresh/" \
     -H "Content-Type: application/json" \
     -d '{"refresh": "YOUR_REFRESH_TOKEN"}'

📌 Running Tests
Run all tests:
python manage.py test

📌 Using Docker (Optional)
If you prefer Docker for the database, use the included docker-compose.yml file.

1️⃣ Start the Database
docker-compose up -d

2️⃣ Update settings.py
Modify DATABASES to use PostgreSQL:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "food_delivery",
        "USER": "admin",
        "PASSWORD": "password",
        "HOST": "db",
        "PORT": "5432",
    }
}

3️⃣ Run Migrations
python manage.py migrate
📌 Future Enhancements
🔹 Implement food rating system and allow users to sort food by rating.
🔹 Add order tracking & estimated delivery updates.
🔹 Improve restaurant search by location.
🔹 Implement WebSocket notifications for real-time updates.

📌 Contributors
Milica Smiljanić