from django import forms
from allauth.account.forms import SignupForm, PasswordField, LoginForm


class CustomSignUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""

        self.fields["username"].widget = forms.TextInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})

        self.fields["password2"].widget = forms.PasswordInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["login"].label = ""
        self.fields["password"].label = ""

        self.fields["login"].widget = forms.TextInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})
        self.fields["password"].widget = forms.PasswordInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})

