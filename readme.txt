1. After you do any change to webpage/webpage/static you need to run:

https://docs.djangoproject.com/en/2.1/ref/contrib/staticfiles/
python manage.py collectstatic

Then if it is running on server, you might need to do:

sudo services apache2 restart

2. After you do any change to models and just after starting a new project/app

python manage.py makemigrations
python manage.py migrate

3. To run local server
python manage.py runserver

4. To access server remotely through file manager:
sftp://almohsen@vision.csee.wvu.edu/home/almohsen/webpage/

5. To ssh to server:
ssh almohsen@vision.csee.wvu.edu
