# Django Task Manager (To-Do App)

A robust, full-stack Task Management application built with **Python** and **Django**. This project demonstrates the implementation of CRUD operations, user authentication, and object-level security.

## 🚀 Key Features
* **User Authentication:** Secure registration, login, and logout functionality using Django's built-in Auth system.
* **CRUD Operations:** Create, Read, Update, and Delete tasks with a clean UI.
* **Task Privacy:** Implemented custom QuerySets to ensure users can only view and edit their own tasks.
* **Status Tracking:** Toggle between 'Complete' and 'Incomplete' states.
* **Search Functionality:** Filter tasks by keywords using Django ORM lookups.

## 🛠️ Tech Stack
* **Backend:** Django (MVT Architecture)
* **Database:** SQLite (Development) / PostgreSQL (Production ready)
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Version Control:** Git & GitHub

## 📂 Project Structure
- `models.py`: Custom Task model with ForeignKey relationship to User.
- `views.py`: Utilized Class-Based Views (ListView, CreateView, UpdateView) for DRY code.
- `settings.py`: Configured for security and static file management.

## ⚙️ Setup & Installation
1. Clone the repository: `git clone [YOUR_URL]`
2. Create a virtual environment: `python -m venv venv`
3. Activate venv: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install django`
5. Run migrations: `python manage.py migrate`
6. Start server: `python manage.py runserver`
