from django import forms
from allauth.account.forms import SignupForm, PasswordField


class CustomSignUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""
