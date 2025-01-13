# Employee Satisfaction Survey App  

This is a Django application for conducting an employee satisfaction survey for the Vihiga County Department of Sports. The app allows users to fill out a form and submit their responses, which are stored in a MySQL database.  

## Features  
- User-friendly survey form.  
- Stores survey responses in a MySQL database.  
- Easy to customize for additional fields or questions.  

---

## Prerequisites  

Before running the application, ensure you have the following installed:  
- Python 3.8+  
- Django 4.0+  
- MySQL Database  
- MySQL client for Python (`mysqlclient`)  

---

## Installation  

1. **Clone the Repository**  
   ```bash
   git clone <repository-url>
   cd employee_survey



python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt

# Update DATABASES in employee_survey/settings.py with your MySQL credentials:
 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vihiga_survey',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


python manage.py makemigrations
python manage.py migrate


python manage.py runserver




