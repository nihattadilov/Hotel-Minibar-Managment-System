Hotel Minibar Management System
Welcome to the Hotel Minibar Management System! This web application helps hotels manage minibar operations, including room management, sales tracking, product inventory, and data export.

Features
Room Management: Add, update, and delete room details.
Sales Tracking: Record and view sales transactions.
Product Management: Manage minibar products including adding, updating, and removing items.
Excel Data Export: Download data for rooms, products, and sales in Excel format.
Technologies Used
Backend: Django (Python Framework)
Frontend: HTML, CSS, JavaScript
Database: SQLite (default; configurable for other databases)
Excel Export: django-import-export library
Installation
To set up the project, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/nihattadilov/Hotel-Minibar-Managment-System.git
cd Hotel-Minibar-Managment-System
Create and Activate a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Apply Migrations:

bash
Copy code
python manage.py migrate
Create a Superuser:

bash
Copy code
python manage.py createsuperuser
Run the Server:

bash
Copy code
python manage.py runserver
Access the app at http://127.0.0.1:8000/.

Usage
Log in to the admin interface at http://127.0.0.1:8000/admin/ with your superuser credentials to manage rooms, products, and sales.
