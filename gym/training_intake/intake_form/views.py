from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientIntakeForm
from .models import ClientIntake
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def intake_form_view(request):
    if request.method == "POST":
        form = ClientIntakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ClientIntakeForm()
    return render(request, 'intake_form.html', {'form': form})


@login_required
def success_view(request):
    return render(request, 'success.html')


@login_required
def view_submitted_requests(request):
    # Fetch all submitted requests from the database
    submissions = ClientIntake.objects.all()
    return render(request, 'submitted_requests.html', {'submissions': submissions})


@login_required
def submission_detail(request, submission_id):
    # Fetch a specific submission by its ID
    submission = get_object_or_404(ClientIntake, id=submission_id)
    return render(request, 'submission_detail.html', {'submission': submission})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Signup successful! Please login.")
        return redirect('login')

    return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('submitted_requests')  # Redirect to a dashboard or home page
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('index')
