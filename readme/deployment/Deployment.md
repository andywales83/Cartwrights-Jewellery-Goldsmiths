# Deployment

***

## Index – Table of Contents

* [Heroku Deployment](#heroku-deployment) 
* [AWS and S3 Bucket Setup](#aws-and-s3-bucket-setup)
* [IAM Setup](#iam-setup)
* [Connecting Django to AWS](#connecting-django-to-aws)
* [Cloning](#cloning)

***


## Heroku Deployment

Although deployed from its GitHub repository, the project is hosted by Heroku. In order to deploy to Heroku, the following steps should be followed:
1. Create an account at [Heroku](https://heroku.com/) and log in.
2. Choose 'create new app' from the drop down menu labelled 'new'.
3. Give the app an appropriate name and choose the closest region from the dropdown list, then click 'create app'.
4. From the 'resources' tab, search for and select Heroku Postgres from the add-ons. Also choose 'Hobby Dev – Free plan'.
5. From the Heroku dashboard, navigate to the 'deploy' tab, 'deployment method' section and select 'connect to GitHub'. 
6. Search for your GitHub repository, click 'connect' and then select 'Automatic Deploys'.
8.	In order for a Django project to be deployed on Heroku, use `pip3 install' to install the following packages from your IDE terminal as follows:
    `pip3 install gunicorn`
    `pip3 install psycopg2-binary`
    `pip3 install dj-database-url`
9.	To make sure the app has all the required modules, run `pip3 freeze > requirements.txt` in your terminal.
10.	Still in the terminal, create a Procfile by typing `web: gunicorn jiira.wsgi:application`
11.	As a fixtures file wasn't used to populate the database, run the following to create a json file for populating the Heroku Postgres database:
    `python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json`
12. In settings.py, comment out the existing SQLite DATABASES and replace the default 'DATABASE' setting with the 'database_url' (found in the app's config vars in Heroku) using the following code:
```
DATABASES = {
        'default': dj_database_url.parse(<DATABASE_URL>)
    }
```
13.	Now connected to the Postgres database, it can be populated by running the following:
`python3 manage.py showmigrations`
`python3 manage.py migrate`
`python3 manage.py loaddata db.json`
14. To be able to login to the Postgres database, create a new superuser (and then follow the instructions in the terminal):
`python3 manage.py createsuperuser`
15. Log into Heroku via your IDE terminal using 'heroku login -i'.
16. So that no static files are transferred, type `heroku config:set COLLECTSTATIC=1 --app <app_name>`
17. In settings.py add the Heroku app's host name:
`ALLOWED_HOSTS = ['<hostname>', 'localhost']`
18. Still in 'settings.py', change the 'DATABASE' section in order that it retrieves the correct value (Heroku Postgres for live, Django SQLite for testing):
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('<DATABASE_URL>'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
19.	In your [Stripe](https://stripe.com/) account, add the Heroku app URL with a new webhook endpoint.
20.	Update 'settings.py' with the new Stripe environment variables and email settings.
21.	Next, Git add, commit and push all changes to GitHub.
22. In the Heroku dashboard, navigate to the 'settings' tab, 'config vars' section and enter the following key value pairs:
```
    * AWS_ACCESS_KEY_ID - AWS access key
    * AWS_SECRET_ACCESS_KEY - AWS secret key
    * DATABASE_URL - Your Postgres database URL 
    * EMAIL_HOST_PASS - Your Email Password (generated through Gmail)
    * EMAIL_HOST_USER - Your Email Address
    * DISABLE_COLLECTSTATIC - Created this during step 16
    * SECRET_KEY - Your Django secret key (I used Djecrety to generate mine)
    * STRIPE_PUBLIC_KEY - Stripe public key
    * STRIPE_SECRET_KEY - Stripe secret key
    * STRIPE_WH_SECRET - Stripe webhook key
    * USE_AWS - True
```
23. The app can now be launched directly from Heroku (or at https://YOUR-APP-NAME.herokuapp.com) and will automatically update to the latest version each time commits are pushed to Github.


## AWS and S3 Bucket Setup

1. Create an [AWS](https://aws.amazon.com/) account (choose the free tier) and login.
2. Navigate to the management console, search for 'S3' to access the S3 dashboard.
3. Click 'create bucket' button
4. Give it a name (same as app name on Heroku), select the region closest to you, allow public access and then click on 'create'.
5. From the dashboard go to the bucket's properties tab, select 'static website hosting' and 'use this bucket to host a website'.
6. Set the home/default page to 'index.html' and error link as 'error.html', then save.
7. On the permissions tab, edit the 'CORS configuration' as follows and save when done:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
8. Go to the bucket policy section and click 'edit' and then 'policy generator'.
9. In the newly opened window, select 'S3 Bucket Policy'
10. Next, set the following options:
    * Allow all principals by using '*'.
    * Set action to 'GetObject'.
    * Amazon Resource Name (ARN) – Copy and paste in the value found on the previous page, under 'Bucket ARN'.
    * Click 'Add statement' and then 'Generate policy' 
    * Copy and paste the json file shown into to bucket policy.
    * Make sure to add '/*' at the end of the 'Resource' key to allow access to all resources.
    * Click 'save'.
11. Navigate to the Access Control List (ACL) tab, set the list objects to 'everyone' under the Public Access section and click 'save'


## IAM Setup

1. Navigate to the AWS management console, search for 'IAM' and open it.
2. Select 'Groups' from the menu, click 'create new group' giving it a relevant name.
3. Select 'Policies' from the menu and then 'create policy'.
4. Select the JSON tab and click the 'import managed policy'.
5. Search for and import 'Amazon S3 Full Access'.
6. Copy your ARN and place it in the code as shown below;
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "arn:aws:s3:::<YOUR-ARN>",
                "arn:aws:s3:::<YOUR-ARN>/*"
            ]
        }
    ]
}
```
7. Click on next until you get to 'review the policy', give it a name and a description and click 'create'.
8. Back on the policy page, navigate to 'user groups' and click 'manage group name'
9. Click 'Attach policies' then search for and select the policy you created in step 8 above.
10. Next, click 'users' from the menu, then 'add user' and give it a relevant name.
11. Give this user 'programmatic access' and add it to the newly created group.
13. Click through 'next' and then 'create user'.
13. Finally, make sure to download the .csv file you see there and save it. This file contains essential secret keys.


## Connecting Django to AWS

1. Install boto3 and django-storages via the terminal in your IDE to connect AWS S3 bucket to Django:
```
pip3 install boto3
pip3 install django-storages
```
2. Run `pip3 freeze > requirements.txt`
3. Add 'storages' to INSTALLED_APPS in settings.py.
4. Open the .csv file you saved from the previous section and copy the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY values to the Config Vars in Heroku.
5. Remove the DISABLE_COLLECTSTATIC variable.
6. Back in your terminal, create a new file called 'custom_storages.py' and enter the following code:
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
7. Go to 'settings.py' and add the following:
```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'jiira'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
8. Lastly, Git add, commit and push all changes to GitHub.


## Cloning

To work on a local copy of the code, use the following steps:
1. Log in to [Github](https://github.com/) and navigate to [GitHub Repo](https://github.com/johnroutledge/milestone-project-4).
2. Click 'code' and then copy the url.
3. In your IDE, open the directory you wish to copy the project.
4. In the terminal, type 'git clone' followed by the url copied in step 2 above and press 'enter'.
5. The clone will be created in your selected directory.
6. Create a new env.py file at the base directory level and copy the following into the created env.py file:
```
import os

#Django
os.environ.setdefault( 'DEVELOPMENT', 'True')
os.environ.setdefault('SECRET_KEY', '<YOUR_KEY>')

#Stripe
os.environ.setdefault('STRIPE_PUBLIC_KEY', '<YOUR_KEY>')
os.environ.setdefault('STRIPE_SECRET_KEY', '<YOUR_KEY>')
os.environ.setdefault('STRIPE_WH_SECRET', '<YOUR_KEY>')
```
7. Be sure to add 'env.py' to the .gitignore file to keep it out of version control
8. Type the following in the terminal to install all the required django modules and dependencies:
`pip3 install -r requirements.txt`
9. Next, create your database by entering the following two commands in the terminal, one after another:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
10. To be able to have admin access, create a superuser using the line below and then following the instructions in the terminal:
`python3 manage.py createsuperuser`

11. The site can now be run locally by entering the following in the terminal:
`python3 manage.py runserver`
