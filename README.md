# TinyML-backend
![GitHub Actions](https://github.com/TinyMLaas/TinyML-backend/actions/workflows/backend_tests.yml/badge.svg)

This is the backend for the [TinyMLaaS](https://github.com/TinyMLaas) project.

## Instructions for running the application

Start by [cloning](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository. Then setup and run the app with the following steps.

## Virtual environment

Setup [venv](https://docs.python.org/3/library/venv.html) with:

```
python -m venv venv
```

Activate the virtual environment with:

```
source venv/bin/activate
```

## Dependencies

Install project dependencies by running the following command inside the virtual environment:

```
pip install -r requirements.txt
```

## Database setup

In a new terminal window, run the following commands to set up an sqlite database:

```
sqlite3
.open tiny_mlaas.db
.read schema.sql
.schema
.read populate.sql
```

To connect the backend to the database, create a .env file (in the project's root directory) with the following line:

```
DATABASE_URL="sqlite:///./tiny_mlaas.db"
```

## Machine learning modules setup



## Run app

With the virtual environment activated in the project's root directory, run the app with:

```
uvicorn main:app --reload
```

## Usage

Use the application with the project frontend [here](https://github.com/TinyMLaas/TinyML-frontend), or explore the API by browsing to: *BACKEND_URL*/docs.

## Testing

Run unit tests with:

```
python -m unittest discover -v
```
