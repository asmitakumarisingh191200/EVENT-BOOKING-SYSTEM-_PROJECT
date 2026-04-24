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
