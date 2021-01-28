from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class EditProfileForm(UserChangeForm):
	password = forms.CharField(label="",  widget=forms.TextInput(attrs={'type':'hidden'}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password','password')

# AGABA JOSHUA
class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="EMAIL", widget=forms.TextInput(attrs={ 'placeholder':'Email Address'}), )
	first_name = forms.CharField(label="FIRST NAME", max_length=100, widget=forms.TextInput(attrs={ 'placeholder':'First Name'}))
	last_name = forms.CharField(label="LAST NAME", max_length=100, widget=forms.TextInput(attrs={ 'placeholder':'Last Name'}))
	Reg_number = forms.CharField(label="REG NO.", max_length=20, widget=forms.TextInput(attrs={ 'placeholder':'18/U/...', 'title':'Enter your Reg number'}))
	student_number = forms.CharField(label="STUDENT NO.", max_length=30, widget=forms.TextInput(attrs={ 'placeholder':'student number', 'title':'Enter your student number'}))
	course_name = forms.CharField(label="COURSE", max_length=200, widget=forms.TextInput(attrs={ 'placeholder':'Your course', 'title':'Enter your Year of study'}))
	year_of_study = forms.CharField(label="YEAR OF STUDY", max_length=4, widget=forms.TextInput(attrs={ 'placeholder':'Year of study'}))
	
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'course_name', 'year_of_study', 'Reg_number','student_number',)

	