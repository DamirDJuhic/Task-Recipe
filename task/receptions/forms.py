import imp
from importlib.abc import ExecutionLoader
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Reception,Rating,Ingredient

class ingredientform(forms.ModelForm):
   class Meta:
      model = Ingredient
      exclude = ("recipe","ingredient",)
      
ingredientformset = forms.inlineformset_factory(Reception,Ingredient,form=ingredientform)

class receptionform(forms.ModelForm):
   class Meta:
      model = Reception
      fields= ('title','author','describe',)
      widgets = {
         'title' : forms.TextInput(attrs={'class':'form-control'}),
         'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
         'describe' : forms.Textarea(attrs={'class':'form-control'}),
         
      }

class Ratingf(forms.ModelForm):
   class Meta:
      model = Rating
      fields = '__all__'