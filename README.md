# asuna
asuna is a healthcare chatbot use to diagnose diseases via symptoms with a simple to use interface for both admins and users

To run the project all you need to do is create a virtual environement in the files : Healthcare chatbot and pytorchChatbot.

Instalation uses the same commands in both files:

( make sure to instal python 3.8 or above and mysql shell before proceeding with the instalation ) 

```console
foo@bar:~$ py -m venv venv
foo@bar:~$ cd /venv/Scripts
foo@bar:~$ activate
foo@bar:~$ (venv) cd..
foo@bar:~$ (venv) cd..
foo@bar:~$ (venv) py -m pip install -r requirements.txt
--instalation Finished
```

for the django app in Healthcare chatbot make sure to migrate to MySQl before running the server
```console
foo@bar:~$ (venv) py manage.py makemigrations
foo@bar:~$ (venv) py manage.py migrate
foo@bar:~$ (venv) py manage.py runserver 8000
```

for the flask chatbot container you can retrain the model if you change the intents.json using the following command (venv activated)

```console
foo@bar:~$ (venv) py train.py
```

the model is already trainned so you can go ahead and run the flask app

```console
foo@bar:~$ (venv) py app.py
```

you can access the app now on localhost:8000/ !

for more informations see the included report
