# Project Management Tool

A full-stack **Django** web application for managing companies, projects, tasks, and teams — built with role-based collaboration features like task assignment, comments, direct messaging, and a friend/invite system.

## Features

- **User Authentication** — registration, login/logout, and session-based auth
- **Company Management** — register companies and associate users/projects with them
- **Project Tracking** — create projects with deadlines, completion percentage, status (`Stuck` / `Working` / `Done`), and team assignment
- **Task Management** — create tasks under projects, assign users, and track due status (`On Due` / `Overdue` / `Done`)
- **Task Collaboration** — per-task comment threads and direct messaging between assigned users
- **User Profiles** — profile pictures, per-user dashboards, and activity context
- **Social/Team Layer** — send, accept, and delete friend invites; manage a friends list
- **Dashboard & Analytics** — overview of users, companies, projects, tasks, and average project completion

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 2.0 (Python 3.8) |
| Database | SQLite (development), PostgreSQL (production via `dj-database-url`) |
| Static/Media Storage | AWS S3 (`django-storages`, `boto3`) |
| Deployment | Heroku (`gunicorn`, `Procfile`) |
| Image Handling | Pillow |
| Forms | Django Forms, `django-multiselectfield` |

## Project Structure

```
├── core/           # Landing page, dashboard, login/logout, global context
├── register/       # User registration, companies, profiles, friends & invites
├── projects/       # Projects, tasks, comments, and messaging
├── manager/        # Django project settings, URLs, WSGI config
├── requirements.txt
├── runtime.txt
└── Procfile        # Heroku deployment config
```

### App Breakdown

- **`core`** — entry point of the app; handles the index page, authenticated dashboard, and login/logout flows. Also defines the global template context processor used across the site.
- **`register`** — owns `Company` and `UserProfile` models, plus the friend/invite system (`Invite` model with `accept()` logic) and profile picture uploads.
- **`projects`** — owns `Project` and `Task` models, along with `Comment` and `Message` models for task-level collaboration.

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Qadeer572/CodeAplha_ProjectManagementTools.git
cd CodeAplha_ProjectManagementTools

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser (for admin access)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

The app will be available at `http://127.0.0.1:8000/`.
 

## Roadmap / Possible Improvements

- Move `SECRET_KEY` and other credentials fully into environment variables
- Add REST API endpoints for frontend integration
- Replace print-based debug logging in views with proper logging
- Add automated test coverage (currently placeholder `tests.py` files)
- Upgrade to a supported Django LTS version


## Author

**Qadeer** — [GitHub](https://github.com/Qadeer572)
