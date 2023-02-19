# Kwitantiebouwer

General webform that calls a PDF generator to make kwitanties. Can be setup to commit all new kwitanties to a GitLab instance.

## Usage
Clone the repository, populate the default values in kwitantie/input_field.py with actual values.

### Local usage

1. Open a terminal in the project directory and install Django and all the dependencies
~~~
pip install -r requirements.txt
~~~
2. Run a migration to create a new sqlite database.
~~~
python manage.py migrate
~~~
3. Start the server
~~~
python manage.py runserver
~~~

### Deploying the app

Use the supplied dockerfile to create a docker image.

.run settings are included for JetBrains IDE's to load local config from.

## Current limitations

Currently setup to use sqlite database, for persistance switch to a database not in the container.
