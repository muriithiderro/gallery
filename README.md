
 # Gallery Application.

 The Gallery App allows a user to view photos i post based on a certain criteria, by category and location.

#### By **Derrick** created on, June 10th 2018 

## Description

This Application is python based ie django web app and runs on any browser on desktop,laptop or phone, It allows a user to view photos based on location or a category. It also a search engine that allows the user to search by a category eg books or location, then once the photos are loaded, the user can click them to view more details.

## Behaviour of the application
### View
All photos are listed on visiting the home page, but on search, photos then are listed based on that category or location.
### Search
A user can search based on categories and locations listed.

### Admin
On the admin side, the admin is responsible for adding photos, deleting and updating various fields

## Development and Setup.

### prerequisites
+ First clone the project to your camputer. ```git clone <repo url>```
+ Ensure python3 is installed.
+ Install virtual environment by running ```pip3 install virtualenv```
+ Create a virtualenvironment by running ``` virtualenv <name of environment>``` on the terminal and once its activated by running ``` source <name of environment>/bin/activate``` then install all the packages by running ```pip3 install -r requirements.txt```
+ Then create a superuser by running ```python manage.py createsuperuser``` so that as an admin yul be able to manage ```CRUD``` operations to the application.
+ Then start the server by running ```python3 manage.py runserver```.
+ Copy the link and paste in any browser ```http://localhost:8000```


### Important packages used in app development.

```
They are listed in the requirements file.

```

## Technology and Tools Used

+ Python3.6 - Programming language
- Django 1.11
- Git - Version control
- Vs code- Code editor
- Postgres - Database

## Test Driven Development

Testing was done using python inbuild test tool called **unittest** to test database connections ,forms and models.

## Further help
To get Further help you can visit the official [python](https://www.python.org/) and [django](https://docs.djangoproject.com ) documentation.

## Licence
MIT (c) 2017 [muriithi derrick](https://github.com/muriithiderro)
