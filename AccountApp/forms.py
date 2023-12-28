from django.forms import ModelForm
from AccountApp.models import User, User_info
from django.contrib.auth.forms import UserCreationForm


class UserInfoForm(ModelForm):
    class Meta:
        model = User_info
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1','password2',)
    