from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, ContactForm


# ─── AUTH VIEWS ───────────────────────────────────────────────────────────────

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    error = None
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        if not email and not password:
            error = 'Email and password are required.'
        elif not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'
        else:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name}!')
                return redirect('home')
            else:
                error = 'Invalid email or password.'

    return render(request, 'login.html', {'error': error})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.create_user()
            login(request, user)
            messages.success(request, f'Account created! Welcome, {user.first_name}!')
            return redirect('home')
        # form.errors will be rendered inline

    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "You've been logged out.")
    return redirect('login')


# ─── PROTECTED PAGES ──────────────────────────────────────────────────────────

@login_required
def home_view(request):
    return render(request, 'home.html', {'user': request.user})


@login_required
def about_view(request):
    return render(request, 'about.html')


@login_required
def contact_view(request):
    success = False
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()                          # persists to SQLite
            messages.success(request, 'Message sent successfully!')
            success = True
            form = ContactForm()                 # reset form

    return render(request, 'contact.html', {'form': form, 'success': success})
