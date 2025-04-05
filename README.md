https://useful-neighbourhood.onrender.com
login: tycoon
password: lexm54321


Name of project: Useful Neighbourhood.


Project overview.

This WEB application was created as part of the homework of Python developer 
study course in the Mate Academy. 
The idea was spontaneous.
The main purpose of the WEB application is to provide platform where neighbours
of one or couple block flat houses can help, assist, and provide services to 
each other.
![](/Users/dmytropetetskiy/PycharmProjects/useful_neighbourhood/static/assets/img/UN_DB_scheme_rs.png)


Configuration.

This WEB application was build using MVT (model view template) pattern of 
DJANGO ORM framework and Django Bootstrap5 template.


Installation instructions

In order to run the project following packages have to be installed:
* asgiref==3.8.1
* black==25.1.0
* click==8.1.8
* crispy-bootstrap4==2024.10
* Django==4.2
* django-crispy-forms==2.3
* django-debug-toolbar==3.2.4
* django-environ==0.12.0
* flake8==5.0.4
* flake8-quotes==3.3.1
* flake8-variables-names==0.0.5
* gunicorn==23.0.0
* h11==0.14.0
* mccabe==0.7.0
* mypy-extensions==1.0.0
* packaging==24.2
* pathspec==0.12.1
* pep8-naming==0.13.2
* platformdirs==4.3.6
* psycopg2-binary==2.9.10
* pycodestyle==2.9.1
* pyflakes==2.5.0
* python-decouple==3.8
* python-dotenv==1.1.0
* sqlparse==0.5.3
* uvicorn==0.34.0
* whitenoise==6.9.0


Operating instructions.

Navigation.
All pages equipped with navigation panel located on the top. The navigation 
options are: Home, Services, Rentals, Requests, Create Account / User Account page,
Login / Logout. Non authenticated users can access only landing page while the other
pages are password protected.

DB consists of 4 models: Neighbour(AbstractUser), Service, Request, Section.
Registered Neighbour can publish, update, delete Services and Requests.
Services and Requests belong to different categories of Category model.
Any registered Neighbour can join any created Service or Request, but only 
author of Service or Request can update or delete them.
Once Service or Request created it automatically assigned to the author.
Services and Requests are listed on respective pages where user can click to title 
of Service or Request and redirect to detail page where user can join Service or remove 
him self from Service. So any Service can have multiple providers as well as Request can 
have multiple assignees.
User can manage all his Services and Requests at his User account page.


Known bugs.

Only the author of Service or Request can delete it. But it is guaranteed by the HTML only.
So any registered user can simply open any detail page of Service or Request add to 
URL update / delete and this way update or delete respective Service, Request and 
even Neighbour from DB.
