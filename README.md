Recipe App

Aim
To build a fully functional Recipe web application, which can create, read and modify recipes, and search for recipes based on ingredients. The web application will include an admin panel for data handling and visualization.

Objective
To develop a full-stack web application using the Django development server. Users will be able to sign in and perform CRUD operations on the database using a Then deploy the application using Heroku, with a Postgres database at
the backend, HTML, and CSS-based rendered pages

Key Features
● Allow for user authentication, login, and logout.
● Let users search for recipes according to ingredients.
● Automatically rate each recipe by difficulty level.
● Receive user input and handle errors appropriately.
● Display more details on each recipe if the user asks for that.
● Add user recipes to an SQLite database.
● Include a Django Admin dashboard for working with database entries.
● Show statistics and visualizations based on trends and data analysis.

Installation
Note: Run these commands in the terminal from the desired root directory

Clone the repo
git clone https://github.com/ksope/Recipe-App.git

Install the requirements
pip install -r requirements.txt

Migrate the database
python manage.py migrate

Run the local server
python manage.py runserver

Demo
Login with username: "user" and password: "c@reerF0undry"
Click on a recipe tile to see its details
Click on the "Records" tab to search recipes by Ingredient (and view either Bar, Pie or Line charts).

Technologies: Python, Django, mySQL, Pandas, matplotlib
