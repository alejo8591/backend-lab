from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	"""
    A form that creates a user, with no privileges, from the given email and
    password.
    """
    def __init__(self, *args, **kwargs):
    	super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    	class Meta:
    		model = CustomUser
    		fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
	"""
	A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    def __init__(self, *args, **kwargs):
    	super(CustomUserChangeForm, self).__init__(*args, **kwargs)

    	class Meta:
    		model = CustomUser
