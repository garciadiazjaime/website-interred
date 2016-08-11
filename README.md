InterRed Insurance Website
====

[![Build Status](https://travis-ci.org/garciadiazjaime/website-interred.svg)](https://travis-ci.org/garciadiazjaime/website-interred)


Technologies:
django


Package Installation
`pip install -r requirements.txt`

Run Server
`cd project`
`python manage.py runserver`

GUI - Admin
http://127.0.0.1:8000/admin

DB Setup
`psql -c 'create database focus'`
`python manage.py migrate`
`python manage.py createsuperuser` (this is the user for access the admin, feel free to type anything)
`python manage.py loaddata data/fixtures/data.json`
`python manage.py loaddata data/survey/data.json`

Drop Database
`psql -c drop database focus`

Deploy project
`fab update`
`git status`
`git diff`
`fab deploy`

sprites
`npm run sprites`

set env
rhc set-env ENV_NAME=VALUE -a app_name
