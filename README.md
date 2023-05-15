# brookssphere

This is my attempt at a web application that shows beginners learning full-stack web development what happens behind the scenes

## Installation

Prerequisites:
Python (version 3.6 or higher)
PostgreSQL (version 9.5 or higher)
pip (package installer for Python)

Clone the repository from GitHub:

```
git clone https://github.com/brooks-mitchell/brookssphere.git
```
```
cd brookssphere
```
Create and activate a virtual environment (optional but recommended):
```
python3 -m venv myenv
source myenv/bin/activate
```

Install the required Python packages using pip:

```
pip install -r requirements.txt
```
Create a PostgreSQL database for the application:

```
createdb mydatabase
```
Open the settings.py file located in yourproject/yourproject/settings.py and modify the database settings according to your PostgreSQL configuration:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Apply the database migrations:

```
python manage.py migrate
```
Running the Application
To run the Django development server and start the application, use the following command:

```
python manage.py runserver
```
Once the server is running, you can access the application by opening your web browser and navigating to http://localhost:8000/.

## Contributing
If you would like to contribute to this project, please follow these steps:

Fork the repository on GitHub.
Create a new branch with a descriptive name:
css
Copy code
git checkout -b my-feature
Make the necessary changes and commit them:
sql
Copy code
git commit -am 'Add new feature'
Push the changes to your forked repository:
perl
Copy code
git push origin my-feature
Open a pull request on the original repository and provide a clear description of the changes you made.
License
This project is licensed under the MIT License. Feel free to modify and distribute it as needed.

Acknowledgments
Thank you for using this Django web application! If you have any questions or need further assistance, please don't hesitate to reach out.
