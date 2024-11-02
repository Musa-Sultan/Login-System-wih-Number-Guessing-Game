# Login System with Number Guessing Game

## Overview
This project consists of a simple user authentication system built with Django, allowing users to sign up, log in, and log out. After logging in, users can play a number guessing game with varying difficulty levels: Easy, Medium, and Hard.

## Features
- User registration with unique username and email validation.
- User authentication (login/logout).
- A number guessing game with three difficulty levels:
  - Easy (1-100, 10 attempts)
  - Medium (1-150, 15 attempts)
  - Hard (1-200, 20 attempts)
- User-friendly messages for feedback during signup and gameplay.
- Reset game functionality after a win or when attempts are exhausted.

## Requirements
- Python 3.6 or higher
- Django 4.2.5 or higher
- SQLite (included with Django)

## Installation

1. **Clone the repository:**
   git clone <repository-url>
   cd <repository-directory>

2. **Create a virtual environment (optional but recommended):**
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies:**
   pip install django

4. **Run migrations:**
   python manage.py migrate

5. **Create a superuser (optional):**
   python manage.py createsuperuser

6. **Run the development server:**
   python manage.py runserver

7. **Access the application:**
   Open your web browser and navigate to http://127.0.0.1:8000/.

## Usage

## User Registration
 - Navigate to the signup page.
 - Fill in the username, email, and password fields.
 - Click "Sign Up" to create an account.

## User Login
 - Navigate to the login page.
 - Enter your username and password.
 - Click "Login" to access the number guessing game.

## Number Guessing Game
 - Choose a difficulty level: Easy, Medium, or Hard.
 - Enter your guesses and receive feedback until you either guess the correct number or run out of attempts.
 - Enjoy the game!

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is open-source and available under the MIT License.

## Acknowledgments
 - Django documentation for guidance on building web applications.
 - Resources on user authentication and game development concepts.
