Name of project: Useful Neighbourhood.


Project overview.

This WEB application was created as part of the homework of Python developer 
study course in the Mate Academy. 
The idea was spontaneous.
The main purpose of the WEB application is to provide platform where neighbours
of one or couple block flat houses can help, assist, and provide services to 
each other.


Configuration.

This WEB application was build using MVT (model view template) pattern of 
DJANGO ORM framework and Django Bootstrap5 template.


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

Only author of Service or Request can delete it. But it is guaranteed by the HTML only.
So any registered user can simply open any detail page of Service or Request add to 
URL update / delete and this way update or delete respective Service, Request and 
even Neighbour from DB.
