from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def strong_password(self, password):
        if re.match(
            r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{10,}$',
            password):
            return password
        else:
            raise ValidationError("Passwords must be at least 10 characters and must include at lease one uppercase letter, one lowercase letter, and one digit.")
