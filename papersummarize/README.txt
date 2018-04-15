papersummarize
==============

Getting Started
---------------

- Install the project in editable mode with its testing requirements.

    pip install -e ".[testing]"

- Run your project's tests.

    pytest

- Run your project.

    pserve development.ini

- Run mongo.

    docker run -d -p 27017:27017 --name ps_mongo mongo:latest

- Rest database.

    python scripts/reset_database.py
