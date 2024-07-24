It looks like you are encountering a couple of issues:

1. **Python-dotenv could not parse statement**: There seems to be an issue with your `.env` file at line 10. 
2. **PostgreSQL Authentication Error**: The database connection for the user "root" is failing due to incorrect password authentication.

Here's how you can address these issues:

### 1. Fixing `.env` Parsing Issue

Open your `.env` file and carefully check the syntax around line 10. Ensure that it follows the `KEY=VALUE` format without any quotes around the values. For example:

```
DATABASE_NAME=mydatabase
DATABASE_USER=myuser
DATABASE_PASSWORD=mypassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 2. Fixing PostgreSQL Authentication Error

Ensure that the database credentials in your `.env` file are correct. You should not use "root" as a database user for PostgreSQL. Instead, create a dedicated user with appropriate permissions. Here’s how you can do it:

#### Creating a PostgreSQL User

1. Access your PostgreSQL shell:

    ```sh
    sudo -u postgres psql
    ```

2. Create a new user:

    ```sql
    CREATE USER myuser WITH PASSWORD 'mypassword';
    ```

3. Create a new database and grant all privileges to the new user:

    ```sql
    CREATE DATABASE mydatabase;
    GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
    ```

#### Updating Django Settings

Make sure your `settings.py` in your Django project has the correct database configuration:

```python
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}
```

After updating your `.env` file and `settings.py`, run the migration commands again:

```sh
python manage.py makemigrations
python manage.py migrate
```

If you encounter further issues, please share the contents of your `.env` file (with sensitive information redacted) and the relevant portion of your `settings.py` for more precise assistance.