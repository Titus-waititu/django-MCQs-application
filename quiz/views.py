from django.shortcuts import render, redirect
from .models import Category, Question, Answer, Testimonial, Ticket, UserQuizHistory
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def signup(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        if pass1 != pass2:
            # Display an error message if the passwords do not match
            messages.error(request, "Passwords do not match!")
            return redirect('/signup/')
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/signup/')
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        # Set the user's password and save the user object
        user.set_password(pass1)
        user.save()
        
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/signin/')
    
    # Render the registration page template (GET request)
    return render(request, 'quiz/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        print(f"Username: {username}, Password: {pass1}")  # Debug
        user = authenticate(username=username, password=pass1)

        if user is not None:
            print("User authenticated")
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('dashboard')
        else:
            print("Authentication failed")

            messages.error(request, 'Bad credentials')
            return redirect('/signin')
    return render(request, 'quiz/signin.html')

def log_out(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('/signin')


def dashboard(request):
    categories = Category.objects.all()
    user = request.user
    return render(request, 'quiz/dashboard.html', {'categories': categories, 'user': user})

def landing(request):
    return render(request, 'quiz/landing.html')

def quiz(request, category_id):
    category = Category.objects.get(id=category_id)
    questions = category.questions.all()
    return render(request, 'quiz/quiz.html', {'category': category, 'questions': questions})

def profile(request):
    user = request.user  # Get the currently logged-in user
    quiz_history = UserQuizHistory.objects.filter(user=user)  # Fetch quiz history for the user
    
    return render(request, 'quiz/profile.html', {
        'user': user,
        'quiz_history': quiz_history,
    })

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserQuizHistory, Question, Answer, Category
from django.db.models import Sum

@login_required
def submit_quiz(request, category_id):
    category = Category.objects.get(id=category_id)
    questions = category.questions.all()
    user = request.user
    total_marks = 0
    score = 0

    # Loop through each question
    for question in questions:
        # Get the selected answer for each question
        selected_answer_id = request.POST.get(f'question_{question.id}')
        if selected_answer_id:
            selected_answer = Answer.objects.get(id=selected_answer_id)
            # Check if the selected answer is correct and calculate the score
            if selected_answer.is_correct:
                score += question.marks
        total_marks += question.marks

    # Calculate percentage
    percentage = (score / total_marks) * 100 if total_marks > 0 else 0

    # Create or update the UserQuizHistory model
    user_instance = request.user  # Make sure this is a User instance, not a SimpleLazyObject
    UserQuizHistory.objects.create(
        user=user,
        category=category,
        score=score,
        total_marks=total_marks,
        percentage=percentage
    )

    # You can render a result page or redirect to another page
    return render(request, 'quiz/result.html', {
        'score': score,
        'total_marks': total_marks,
    })




def ticket(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        desc = request.POST['desc']
        tickets = Ticket(
            full_name = full_name,
            email = email,
            subject = subject,
            desc = desc,

        )
        tickets.save()

    return render(request, 'quiz/ticket.html')
    
def testimonial(request):
    if request.method == "POST":
        text = request.POST['text']

        texts = Testimonial(
            text=text
        )
        texts.save()
    
    return render(request, 'quiz/testimonial.html',)


def userquizhistory(request):
    if request.method == 'POST':
        user = request.user
        category = Category.objects.get(id=request.POST['category'])
        score = int(request.POST['score'])
        total_marks = int(request.POST['total_marks'])
        percentage = (score / total_marks) * 100

        user_quiz_history = UserQuizHistory(
            user=user,
            category=category,
            score=score,
            total_marks=total_marks,
            percentage=percentage,
        )
        user_quiz_history.save()
 