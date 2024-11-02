from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random


@login_required(login_url='login')

def home(request):
    return render(request, 'home.html')

def LoginPage(request):
    if request.method == 'POST':
        user_name=request.POST.get('username')
        pas=request.POST.get('password')

        user = authenticate(request, username=user_name, password=pas)
  
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'sign_in.html', {'content': 'Authentication failed user name and password is incorrect.'})
    return render(request, 'sign_in.html')

def SignupPage(request):
    if request.method=='POST':
        user_name=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm_password')
        

        # Check if the username already exists
        if User.objects.filter(username=user_name).exists():
            return render(request, 'sign_up.html', {'content' : 'Username already exists. Please choose a different one.'})  # Render the signup page again
        
        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'sign_up.html', {'content' : 'Email already exists. Please use a different email.'})
        
        if pass1!=pass2:
            return render(request, 'sign_up.html', {'content': 'The password and the confirm password is not same'})
        else:
            my_user=User.objects.create_user(user_name, email, pass1)
            my_user.save()
            return redirect('login')
        
    return render(request, 'sign_up.html')

def Logout(request):
    logout(request)
    return redirect('login')

# def process_guess(request, min_number, max_number, max_attempts, template_name):
#     # Initialize or retrieve game state from session
#     if request.method == 'POST' and 'submit' in request.POST:
#         try:
#             number = int(request.POST.get('guessNumber'))
#         except ValueError:
#             return render(request, template_name, {'text': 'Please enter a valid number.'})

#         # Initialize session variables if not set
#         if 'winning_number' not in request.session:
#             request.session['winning_number'] = random.randint(min_number, max_number)
#             request.session['attempts_left'] = max_attempts
#             request.session['previous_guesses'] = []

#         winning_number = request.session.get('winning_number')
#         attempts_left = request.session.get('attempts_left', max_attempts)
#         previous_guesses = request.session.get('previous_guesses', [])

#         if number in previous_guesses:
#             text = 'You have already guessed that number. Try a different one.'
#         elif number == winning_number:
#             text = f'Congratulations! You guessed the number {winning_number} correctly in {max_attempts - attempts_left + 1} attempts.'
#             request.session.flush()  # Reset game
#         else:
#             attempts_left -= 1
#             if attempts_left <= 0:
#                 text = f'Sorry, you\'ve used all attempts. The winning number was {winning_number}.'
#                 request.session.flush()  # Reset game
#             else:
#                 if number < winning_number:
#                     text = f'Too low! You have {attempts_left} attempts left.'
#                 else:
#                     text = f'Too high! You have {attempts_left} attempts left.'
#                 request.session['attempts_left'] = attempts_left

#             previous_guesses.append(number)
#             request.session['previous_guesses'] = previous_guesses
#     else:
#         text = ''
#         attempts_left = max_attempts
#         previous_guesses = []

#     return render(request, template_name, {
#         'text': text,
#         'previous_guesses': previous_guesses,
#         'attempts_left': attempts_left
#     })

# def EasyPage(request):
#     return process_guess(request, 1, 100, 10, 'easy.html')

# def MediumPage(request):
#     return process_guess(request, 1, 150, 15, 'medium.html')

# def HardPage(request):
#     return process_guess(request, 1, 200, 20, 'hard.html')


import random
from django.shortcuts import render

def EasyPage(request):
    min_number, max_number, max_attempts = 1, 100, 10
    if request.method == 'POST' and 'submit' in request.POST:
        try:
            number = int(request.POST.get('guessNumber'))
            if number < min_number or number > max_number:
                return render(request, 'easy.html', {'text': f'Please enter a number between {min_number} and {max_number}.'})
        except ValueError:
            return render(request, 'easy.html', {'text': 'Please enter a valid number.'})

        if 'winning_number' not in request.session:
            request.session['winning_number'] = random.randint(min_number, max_number)
            request.session['attempts_left'] = max_attempts
            request.session['previous_guesses'] = []

        winning_number = request.session['winning_number']
        attempts_left = request.session['attempts_left']
        previous_guesses = request.session['previous_guesses']

        if number in previous_guesses:
            text = 'You have already guessed that number. Try a different one.'
        elif number == winning_number:
            text = f'Congratulations! You guessed the number {winning_number} correctly in {max_attempts - attempts_left + 1} attempts.'
            request.session.flush()  # Reset game
        else:
            attempts_left -= 1
            if attempts_left <= 0:
                text = f'Sorry, you\'ve used all attempts. The winning number was {winning_number}.'
                request.session.flush()  # Reset game
            else:
                text = 'Too low!' if number < winning_number else 'Too high!'
                text += f' You have {attempts_left} attempts left.'
                request.session['attempts_left'] = attempts_left

            previous_guesses.append(number)
            request.session['previous_guesses'] = previous_guesses
    else:
        text = ''
        attempts_left = max_attempts
        previous_guesses = []

    return render(request, 'easy.html', {
        'text': text,
        'previous_guesses': previous_guesses,
        'attempts_left': attempts_left
    })

def MediumPage(request):
    min_number, max_number, max_attempts = 1, 150, 15
    if request.method == 'POST' and 'submit' in request.POST:
        try:
            number = int(request.POST.get('guessNumber'))
            if number < min_number or number > max_number:
                return render(request, 'medium.html', {'text': f'Please enter a number between {min_number} and {max_number}.'})
        except ValueError:
            return render(request, 'medium.html', {'text': 'Please enter a valid number.'})

        if 'winning_number' not in request.session:
            request.session['winning_number'] = random.randint(min_number, max_number)
            request.session['attempts_left'] = max_attempts
            request.session['previous_guesses'] = []

        winning_number = request.session['winning_number']
        attempts_left = request.session['attempts_left']
        previous_guesses = request.session['previous_guesses']

        if number in previous_guesses:
            text = 'You have already guessed that number. Try a different one.'
        elif number == winning_number:
            text = f'Congratulations! You guessed the number {winning_number} correctly in {max_attempts - attempts_left + 1} attempts.'
            request.session.flush()  # Reset game
        else:
            attempts_left -= 1
            if attempts_left <= 0:
                text = f'Sorry, you\'ve used all attempts. The winning number was {winning_number}.'
                request.session.flush()  # Reset game
            else:
                text = 'Too low!' if number < winning_number else 'Too high!'
                text += f' You have {attempts_left} attempts left.'
                request.session['attempts_left'] = attempts_left

            previous_guesses.append(number)
            request.session['previous_guesses'] = previous_guesses
    else:
        text = ''
        attempts_left = max_attempts
        previous_guesses = []

    return render(request, 'medium.html', {
        'text': text,
        'previous_guesses': previous_guesses,
        'attempts_left': attempts_left
    })

def HardPage(request):
    min_number, max_number, max_attempts = 1, 200, 20
    if request.method == 'POST' and 'submit' in request.POST:
        try:
            number = int(request.POST.get('guessNumber'))
            if number < min_number or number > max_number:
                return render(request, 'hard.html', {'text': f'Please enter a number between {min_number} and {max_number}.'})
        except ValueError:
            return render(request, 'hard.html', {'text': 'Please enter a valid number.'})

        if 'winning_number' not in request.session:
            request.session['winning_number'] = random.randint(min_number, max_number)
            request.session['attempts_left'] = max_attempts
            request.session['previous_guesses'] = []

        winning_number = request.session['winning_number']
        attempts_left = request.session['attempts_left']
        previous_guesses = request.session['previous_guesses']

        if number in previous_guesses:
            text = 'You have already guessed that number. Try a different one.'
        elif number == winning_number:
            text = f'Congratulations! You guessed the number {winning_number} correctly in {max_attempts - attempts_left + 1} attempts.'
            request.session.flush()  # Reset game
        else:
            attempts_left -= 1
            if attempts_left <= 0:
                text = f'Sorry, you\'ve used all attempts. The winning number was {winning_number}.'
                request.session.flush()  # Reset game
            else:
                text = 'Too low!' if number < winning_number else 'Too high!'
                text += f' You have {attempts_left} attempts left.'
                request.session['attempts_left'] = attempts_left

            previous_guesses.append(number)
            request.session['previous_guesses'] = previous_guesses
    else:
        text = ''
        attempts_left = max_attempts
        previous_guesses = []

    return render(request, 'hard.html', {
        'text': text,
        'previous_guesses': previous_guesses,
        'attempts_left': attempts_left
    })
