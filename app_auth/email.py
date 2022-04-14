from djoser import email


class ActivationEmail(email.ActivationEmail):
    template_name = 'email/activation.html'

class PasswordResetEmail(email.PasswordResetEmail):
    template_name = 'email/password_reset.html'