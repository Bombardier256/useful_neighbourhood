# useful_neighbourhood

The main purpose of this website is to provide platform where neighbours 
of one or couple block flat houses can help, assist and provide services to 
each other.
DB consists of 4 models: Neighbour(AbstractUser), Service, Request, Section.
Registered neighbour can publish, update, delete Services and Requests.
Services and Requests may belong to different categories of Category model.
Any registered Neighbour can join any created Service of Request, but only 
author of Service or Request can update or delete them.
