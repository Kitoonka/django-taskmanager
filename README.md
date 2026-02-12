# Django Task Manager

A fully functional **Task Manager** built with **Django**.  
This project allows users to manage tasks efficiently with features like creating, updating, deleting, marking tasks complete, setting priority levels, due dates, and filtering tasks. The UI is enhanced using **Bootstrap** for a clean and professional look.


## Features

- **User Authentication**: Login and logout functionality.
- **Create Tasks**: Add new tasks with a title, due date, and priority.
- **Update Tasks**: Edit task details easily.
- **Delete Tasks**: Remove tasks when they are no longer needed.
- **Mark Tasks Complete**: Keep track of completed and incomplete tasks.
- **Task Filtering**: Sort tasks by status (complete/incomplete) and priority.
- **Search Tasks**: Quickly find tasks by title.
- **Responsive UI**: Built with Bootstrap for a clean and professional appearance.



## Screenshots
Here are some screenshots of the app in action:

[Task List](taskmanager/screenshots/2026-02-12 18_56_02-Grammarly Anchor Window.png)
[Task Form](taskmanager/screenshots/2026-02-12 18_56_26-My Tasks.png)


## Installation
1.Clone the repository
```bash
git clone https://github.com/Kitoonka/django-taskmanager.git
cd django-taskmanager


2.Create a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux


3.Install dependencies
pip install -r requirements.txt


4.Apply database migrations
python manage.py makemigrations
python manage.py migrate


5.Run the development server
python manage.py runserver


6.Open the app in your browser
http://127.0.0.1:8000/tasks/


Usage
Create Tasks: Click "Create New Task" and enter title, due date, and priority.
Edit Tasks: Click "Edit" next to a task to update it.
Delete Tasks: Click "Delete" to remove a task.
Mark Complete: Click the tick icon (✔) to mark a task as completed.
Filter & Search: Use the filter options to sort by priority or completion status.


Dependencies
Django==3.1.8
django-timezone-field==4.2.3
django-celery-beat==2.1.0
Celery==4.4.7
Redis==3.5.3
MySQL-connector-python==9.1.0 (optional if using MySQL)
Bootstrap (via CDN)
Other packages as listed in requirements.txt


Contributing
Contributions are welcome! If you want to improve the project:
1.Fork the repository
2.Create a new branch
3.Make your changes
4.Submit a pull request



This project is open-source and free to use.

Author
Stella Kitoonka
GitHub: https://github.com/Kitoonka