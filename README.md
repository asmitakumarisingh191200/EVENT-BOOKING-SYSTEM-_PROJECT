📌 Event Booking System

A full-stack web application built using Django that allows users to explore events and book tickets seamlessly, with secure authentication and admin management features.

🚀 Features
🔐 User Authentication (Signup, Login, Logout)
📅 View Upcoming Events
🎟️ Book Tickets with real-time availability check
📉 Automatic ticket count update after booking
👨‍💼 Admin Panel to manage events and bookings
🎨 Responsive and user-friendly UI
🛠️ Tech Stack
Backend: Django (Python)
Frontend: HTML, CSS, Django Templates
Database: SQLite (Django ORM)
Authentication: Django built-in auth system
📂 Project Structure
event_booking/
│── event_booking/      # main project folder
│── events/             # app folder
│   ├── models.py       # Event & Booking models
│   ├── views.py        # business logic
│   ├── urls.py         # routing
│   ├── templates/      # HTML files
│── db.sqlite3          # database
│── manage.py
⚙️ Installation & Setup
Clone the repository
git clone <your-github-link>
cd event_booking
Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
Install dependencies
pip install django
Apply migrations
python manage.py makemigrations
python manage.py migrate
Create superuser (Admin)
python manage.py createsuperuser
Run the server
python manage.py runserver
🌐 Usage
Open: http://127.0.0.1:8000/
Signup → Login → View Events
Book tickets for available events
Admin can manage events via /admin/
🔒 Authentication Flow
New users must sign up first
Then login to access events
Only authenticated users can book tickets
📊 Database Integration
Events and bookings are stored using Django models
Real-time updates for ticket availability
Efficient data handling using Django ORM
📸 Screenshots (Optional)

Add screenshots of your project UI here

📌 Future Enhancements
Online payment integration
Email confirmation after booking
Event search and filter options
User booking history
👩‍💻 Author

Asmita Singh
