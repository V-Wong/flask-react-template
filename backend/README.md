# backend
## Project Structure
- ``blueprints/``: This folder contains all the Flask blueprints which groups logically related routes.
- ``connections/sql.py``: This file contains the SQLAlchemy connection. This file is unlikely to ever need modifications.
- ``models/__init__.py``: This file contains the SQLAlchemy models used for object relational mapping.
- ``schemas/__init__.py``: This file contains the schemas which are used to validate Flask JSON request data.
- ``config.py:`` This file reads in and exports out the relevant environment variables for the database connection.
- ``app.py``: This file is the entry point for the backend server. There should be minimal functionality written in this file. Instead this file is mainly for importing functionality written in other files.
