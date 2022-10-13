## Table of content
1. About the API
2. Prerequisites
3. Installation
4. Starting the project
### 1. About the API
***
The goal of the API is to let users create a project. For each project, the author of
the project can add as many contributors as he/she wants. Note that only the author of
the project is allowed to add contributors. Of course, a user can also create as many
projects as he/she wants. Within a project, the author and the contributors can create
issues associated to the project. For each issue, the author of the project and
the contributors can make comments. 
***
### 2. Prerequisites
***
For this project, Django 4.1.2, Django Rest Framework 3.13.1, GitHub and Python 3.10
are required.
***
### 3. Installation
***
In order to install Django Rest Framework, you need first to install Django. Before 
to install Django, make sure your virtual environment is activated. 
If your virtual environment is not activated run the following 
command "env/bin/activate" in the directory you intend to start the project
(in the terminal of your IDE). In the directory, you intend to start your project, 
install Django by running the following command in the terminal of your IDE: 
pip install django. Once Django is installed,create a file named requirements.txt
and add Django(and his version) and Django Rest Framework(and his latest release) 
in the requirements.txt file. Afterwards, go to the terminal of your IDE(still
in the directory you started your Django project) and run the following command:
pip install -r requirements.txt.
***
### 4. Starting the project
***
Once you have successfully installed Django and Django Rest Framework, you can clone
the project by using git clone or git pull with the following address: 
https://github.com/Kmenguete/OpenClassroom_project10.git. When you pulled the project
in your local machine, you have two choices:

-You can use Postman(or any other platform
you fill comfortable with) to work with the API and test every endpoint.

-Or you can use the default Django Rest Framework website.
