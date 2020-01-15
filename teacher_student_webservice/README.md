This repository is dedicated to perform all the required Teacher-Student-Webservice backend actions.

## prerequisites

- Django==3.0.2
- djangorestframework==3.11.0
- 
## Request & Response

For all it's request and response end points, please refer the following sheet:

[Request/Response](https://docs.google.com/spreadsheets/d/1EHZDpL8x8YoexkFRhkAL1QEAwiFLYh-3f-m_6jnBU30/edit?usp=sharing)

## Running Steps

To run the service in local machine, follow the following steps:

    1. Create virtualenv, so that you can use it in future without any trouble 
         python3 -m venv <env_name>
    2. Activate the virtual env you have created
         source <env_name>/bin/activate
    3. pip3 install -r requirements.txt
    4. python3 manage.py makemigrations
    5. python3 manage.py migrate
    6. python3 manage.py runserver


After this, you can refer above sheet and try hitting the api with the proper url.