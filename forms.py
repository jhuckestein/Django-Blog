from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#Now we will create a new form that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()  #default for this method is required=True
	
	class Meta:  #Meta gives us a nested namespace for configurations and keeps them in one place.
	             #So when we do a save it will be saved to User model.  The fields we
				 #see in the list are the fields we want in the form in what order.
		model = User #because we are creating a user and want to interact with this model
		fields = ['username', 'email', 'password1', 'password2']
		
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ['username', 'email']
		
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']