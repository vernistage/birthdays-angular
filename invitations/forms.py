# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
from django import formsfrom django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationgForm):
    first_name = forms.CharField(max_length=100, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=100, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')
    birth_date = models.DateField(required=True, help_text='Required. Input your birthday.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2', )
