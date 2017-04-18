from django.forms import ModelForm
from .models import Meal
from .models import Trip
from django import forms
from django.contrib.auth.models import User


class UserForm(ModelForm):
	class Meta:
		model = User;
		fields = ['username', 'email', 'password', 'first_name', 'last_name']


class ConfirmForm(forms.Form):
	confirm = forms.CharField(max_length=30)

# class MealForm(ModelForm):
# 	Date = forms.DateField(input_formats=['%m-%d-%y'])
# 	class Meta:
# 		model = Meal;
# 		fields = ['Date', 'Breakfast_No_Tip', 'Breakfast_Tip', 'Lunch_No_Tip', 'Lunch_Tip', 'Dinner_No_Tip','Dinner_Tip',]

class MealForm(ModelForm):
	Date = forms.DateField(input_formats=['%m-%d-%y'])
	class Meta:
		model = Meal;
		fields = ['Meal_Category', 'Date', 'Meal_No_Tip', 'Meal_Tip']

class TripForm(ModelForm):
	Date_Left = forms.DateField(input_formats=['%m-%d-%y'])
	Date_Returned = forms.DateField(input_formats=['%m-%d-%y'])
	Time_Left = forms.TimeField(input_formats=['%H:%M'])
	Time_Returned = forms.TimeField(input_formats=['%H:%M'])
	class Meta:
		model = Trip;
		fields = [ 'Username', 'Place', 'Purpose', 'Date_Left', 'Time_Left', 'Date_Returned', 'Time_Returned', 'Contact_Person']
