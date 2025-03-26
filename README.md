# LIBRARY MANAGEMENT SYSTEM API

**Project Type**    RESTFULL API

## How to Setup and Run This Project?

### CLONE REPOSITORY

```bash
$ git clone <remote_repo> (ex: git clone https://github.com/perdanaph/api-library-management.git)
# clone github repository 
```

### SETTING VENV PYTHON

```bash
# Create venv
$ python -m venv <yourenvname> (ex: myenv)
# Activate venv
$ ./<yourenvname>/Scripts/activate 
(ex: ./myenv/Scripts/activate)
# setting venv in your local computer
```

### INSTALL DEPENDENCIES

- before this step, make sure your venv activated
- for example

```powershell
(env) C:\User\<Name>\directory\..\example>
```

#### Install dependencies in file requirements.txt

```bash
$ pip install -r requirements.txt
# install all dependencies
```

#### Setting .env file

Rename file .env.example to .env and fill the variables to connect to your database

example:

```powershell
DATABASE_URL=postgresql://username:password@host:port/<dbname>
```

#### Import file SQL DATABASE

Open your GUI database postgres like PGAdmin or DBeaver, and then import file in existing project file name (data.sql)

#### Check connection database

To make sure your database connection success please run in the terminal this command

```powershell
flask check-db
```

## HOW TO RUN?

To run the project run file app.py in root directory

```powershell
$ python app.py
```

## DOCS ENDPOINT API

| name                     | docs                                                |
| ------------------------ | --------------------------------------------------- |
| Endpoint DOCS            | [api](./docs/docs-api.md)                           |
