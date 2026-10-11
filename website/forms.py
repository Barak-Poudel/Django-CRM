from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email",
            }
        )
    )

    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your first name",
            }
        )
    )

    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your last name",
            }
        )
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Username
        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "User Name"
        })
        self.fields["username"].label = ""
        self.fields["username"].help_text = (
            '<small class="form-text text-muted">'
            '150 characters or fewer. Letters, digits and @/./+/-/_ only.'
            '</small>'
        )

        # Password1
        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Password"
        })
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = (
            '<small class="form-text text-muted">'
            'At least 8 characters, not too common, and not entirely numeric.'
            '</small>'
        )

        # Password2
        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Confirm Password"
        })
        self.fields["password2"].label = ""
        self.fields["password2"].help_text = (
            '<small class="form-text text-muted">'
            'Enter the same password again for verification.'
            '</small>'
        )

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        label="",   
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control'
            }
        )
    )
    email = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control'
            }
        )
    )
    phone = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Phone',
                'class': 'form-control'
            }
        )
    )
    address = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Address',
                'class': 'form-control'
            }
        )
    )
    city = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'City',
                'class': 'form-control'
            }
        )
    )
    state = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'State',
                'class': 'form-control'
            }
        )
    )
    zipcode = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Zipcode',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Record
        exclude = ("User",)
