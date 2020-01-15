from django import forms
from django.forms import ModelForm
from .models import *

class userForm(ModelForm):

	class Meta:
		model = user_info

		fields=['name','username','password','phone_no','address','user_type']

