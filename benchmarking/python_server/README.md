## Details
Language: Python
Version: Python 2.7.6

Framework: Django
Version: Django (1.7)

Packages used: psycopg2

## Instructions:

In the server.go script:
	- Provide the Credentials for the Database in the script pyserver/config.py
	- The CRUD queries can be changed
	- Start the server via `python manage.py runserver` command
	- The server runs at: `http://127.0.0.1:8000`

## API's
	- GET API to perform psql CRUD operations at `127.0.0.1:8000/pyserver/crud`
	- GET API to sleep for `a` seconds at `127.0.0.1:8000/pyserver/time_block?seconds=a`
