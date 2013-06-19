# Lassie Constellation

An adventure game engine that may never be... this is just a hobby repo. Nothing serious (for now).

## Setup

1. Create a virtualenv.
2. Clone repo into virtual env, install requirements.
3. Start postgres server, add "lassie" database.
4. Sync the database `python manage.py syncdb`
5. Copy "env-template" file, rename to ".env"
6. Install Heroku toolbelt.
7. `foreman start`