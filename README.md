# Steps to create a Django Project

1. Create a folder for the new project
2. Open VS Code and a terminal at that project
3. Create the virtual environment

    python -m venv venv

4. Activate the venv

    .\venv\Scripts\activate

5. Install the required dependencies 

    - Both OS: pip install django 

6. Create the django project (One time only command)

    -Both OS: django-admin startproject NAME_FOLDER .
    Expectation is: config folder, venv folder and manage.py file

7. Update settings.py to recognize **static** and **template** path
    expectation: templates and static folders are created

    7.1 inside of static folder create subfolders js, css, img

8. Adding misc files: .gitignore, README.md

9. To generate the requirements.txt file:

    - Both OS: pip freeze > requirements.txt 

# Creating Django apps
1. To create a django app:

    - Both OS: python manage.py start"# blog" 
