from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import ContactMessage


# ─── SIGNUP FORM ──────────────────────────────────────────────────────────────
class SignupForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        min_length=2,
        label='Full Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Your full name',
            'class': 'form-input',
            'autocomplete': 'off',
        }),
        error_messages={
            'required': 'Name is required.',
            'min_length': 'Name must be at least 2 characters.',
        }
    )

    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={
            'placeholder': 'you@example.com',
            'class': 'form-input',
            'autocomplete': 'off',
        }),
        error_messages={
            'required': 'Email is required.',
            'invalid': 'Enter a valid email address.',
        }
    )

    password = forms.CharField(
        min_length=6,
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Min. 6 characters',
            'class': 'form-input',
            'id': 'id_password',
        }),
        error_messages={
            'required': 'Password is required.',
            'min_length': 'Password must be at least 6 characters.',
        }
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Re-enter your password',
            'class': 'form-input',
            'id': 'id_confirm_password',
        }),
        error_messages={
            'required': 'Please confirm your password.',
        }
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email is already registered.')
        return email

    def clean(self):
        cleaned = super().clean()
        pw = cleaned.get('password')
        cpw = cleaned.get('confirm_password')
        if pw and cpw and pw != cpw:
            self.add_error('confirm_password', 'Passwords do not match.')
        return cleaned

    def create_user(self):
        """Creates and returns the new User instance."""
        data = self.cleaned_data
        user = User.objects.create_user(
            username=data['email'],          # use email as unique username
            email=data['email'],
            password=data['password'],
            first_name=data['name'],
        )
        return user


# ─── CONTACT FORM ─────────────────────────────────────────────────────────────
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'form-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'you@example.com',
                'class': 'form-input',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'How can we help?',
                'class': 'form-input',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Tell us more...',
                'class': 'form-input',
                'rows': 5,
            }),
        }
        error_messages = {
            'name':    {'required': 'Name is required.'},
            'email':   {'required': 'Email is required.', 'invalid': 'Enter a valid email.'},
            'subject': {'required': 'Subject is required.'},
            'message': {'required': 'Message is required.'},
        }

    def clean_message(self):
        msg = self.cleaned_data.get('message', '')
        if len(msg.strip()) < 10:
            raise ValidationError('Message must be at least 10 characters.')
        return msg
