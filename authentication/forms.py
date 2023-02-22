from django import forms
from . import models
from allauth.account.forms import SignupForm, PasswordField, LoginForm


class CustomSignUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"] = forms.CharField(max_length=5)

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

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignUpForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user


# class StudentProfileSignUp(forms.ModelForm):
#     class Meta:
#         model = models.StudentProfile
#         fields('')


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

