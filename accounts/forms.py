from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # custom label
        self.fields['username'].label = 'Name'
        self.fields['email'].label = 'Email Address'
