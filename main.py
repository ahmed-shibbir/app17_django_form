# install Django in terminal
# Set up Django project in terminal : django-admin startproject mysite .
# In the above command, mysite is the folder name. The dot indicates that the folder will be added in the current directory
# This will create configuration files of the main project and manage.py file. These are usually not required to be changed except in some cases like settings file where every new app is added under INSTALLED APPS ditionary and TEMPLATES('DIRS': [], if you do not provide html file path here, django will assume html file is in  te templates folder(to be manually created),. You need to save the changes in this file by ctrl+s or save option.
# So django project is created through above command. Now we need to create django app in the terminal
# The command for app is: python manage.py startapp job_application
# job-application is the folder which is the app. the folder contains configuration files of the app, not project. Configuration files of the project is located in mysite folder.
# You can create multiple app in a project. Our current app is the job_application app.
# Python uses manage.py file to create app. Manage.py file was created when creating the project-it is part of the project.
# Running app is django is done in the terminal with following command: python manage.py runserver This is as opposed to flask app-which is run through main.py or app.py file.
# This will create an url for a website

# STEPS SUMMARY:-
## pip install django
## django-admin startproject mysite .
##  python manage.py startapp job_application
## python manage.py runserver
## NEXT STEP IS TO CREATE AN index.html file which will act as the homepage

## now we need to start coding our app. the approach is bottom up-starting from database(backend), the code python files, then code the front end-which is the html, css and boostrap.

## NOW CRATE A DATABASE MODEL. TO CREATE DATABASE MODEL YOU NEED TO STOP THE RUNNING APP BT CTRL C IN THE TERMINAL, THIS WILL RETURN TO NOMAL PROMPT UNDER VENV.
## A model.py is already created within job_aaplication folder when app was created. open that file, delete any comment line, and create the model with a class
## To [populate sb.sqlite3 from model.py file, we need to migrate data from model.py to db.

## NEXT-MIGRATE:  python manage.py makemigrations

## this command will populate __iniy__.py file in migrations folder in the job_application folder.
## This will create 0001_initial.py file in migrations folder by codifying all model.py data in the python codes(translated model.py class/data into python code)
## This 0001_initial.py file is like a middle man between Form class and the database db.sqlite3
## NEXT STEP To transfer this data from 0001_initial file to database: python manage.py migrate
## THIS WILL CREATE 12 TABLES IN THE DATABASE. ONE OF THEN IS job_application_form, which has model.py data.
## only job_application_fprm table relates to the app. other 11 tables relate to the project-which creates configuration for the project.
## THIS CREATED THE TABLE STRUCTURE/ COLUMN FIELD IN THE DATABASE. ACTUAL DATA WILL BE CREATED AFTER THE USER INPUTS DATA IN THE FOLM.
## IF NOW YOU WANT TO ADD ANOTHER FIELD TO THE MODEL, YOU NEED TO RUN MAKE MIGRATIONS AGAIN, WHICH WILL CREATE A NEW INITIAL.PY FILE. aFTER RUNNING migrate command as before, the changes will be updated in the database.

## NEXT STEP-update views.py file. UPDATE THE WEB PAGE THROUGH VIEW FUNCTION(index function in flask app, in django it is called view function which populates webpage) AND HTML

## index function in views.py file will return render_template, in django it is just return render

## FOR EMAIL, DO THE FOLLOWING IN settings.py file aadter DEFAULT_AUTO_FIELD:
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    #
    # EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    # EMAIL_HOST = "smtp.gmail.com"
    # EMAIL_PORT = 587
    # EMAIL_USE_TLS = True
    # EMAIL_HOST_USER = "shibbirahmedd@gmail.com"
    # EMAIL_HOST_PASSWORD = "app password-will be provided later"

