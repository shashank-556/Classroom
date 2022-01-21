# Classroom
Restful Web API implemented in django for a classroom application similar to Google Classroom <br>
[Here](http://shashankkkkk.pythonanywhere.com/) is the link of the for the backend api. <br>
The project uses **djangorestframework-simplejwt** for authorization and **MySQL** as its backend database.

## Installation

It is advisable to first create a virtual environment for this project. Then proceed with installation
```console
# clone the repo
$ git clone https://github.com/shashank-556/Classroom.git

# change the working directory to Classroom
$ cd Classroom

# install the requirements
$ python3 -m pip install -r requirements.txt
```
## Databse setup
Create a secrets.json file (in the same folder with manage.py) with following keys:
```json
{
    "SECRET_KEY": "",
    "DB_PASSWORD": "",
    "DB_USER": "",
    "DB_NAME": "",
    "DB_HOST": "",
    "DB_PORT": ""
}
```
SECRET_KEY is the django-project secret key which is used in cryptographic signing. You can generate a secret key by creating a dummy or temporary django project (you can find it in settings.py).<br>
Rest of the keys are related to your database. You can use SQLite by changing the DATABASES object in settings.py. In that case you won't need all the DB_ keys.


