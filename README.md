# iih-Task - Simple Django App

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)

This is a job portal app that allows users to search and view job listings.
The project is structured with `pypoetry` for dependency management and includes a PostgresSQL database for storing job
data.

## Project Setup

### Prerequisites

- Python 3.11+
- PostgresSQL
- [Poetry](https://python-poetry.org/): For managing Python dependencies.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/abdalkreemorabi/django-job-portal.git
   cd django-job-portal
   ```

2. **Set Up the Virtual Environment**
   ```bash
      poetry install
   ```

3. **Activate the Virtual Environment**
   ```bash
      poetry shell
   ```

4. **Configure the Environment Variables**
   <br>Create a .env file in the root directory of your project and add the following configuration:
      ```
      SECRET_KEY=your-secret-key
      DEBUG=True
   
      DB_NAME=jobs
      DB_USER=orabi
      DB_PASSWORD=1234
      DB_HOST=localhost
      DB_PORT=5432
      ```

5. **Apply Migrations**
    ```bash
     python manage.py migrate
    ```

6. **Create Super User to access the app**
    ```bash
     python manage.py createsuperuser
    ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

- The server will start at http://127.0.0.1:8000/.
<br>
- Example from jobs page:

![examplejobs](/jobs/static/images/example_jobs.png)
