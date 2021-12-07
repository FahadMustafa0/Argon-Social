from django import forms 
from .models import profile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
   
    class Meta:
        model = profile 
        fields = [ 
            'first_name',
            'last_name',
            'bio',
            'email',
            'country',
            'avatar',
            'friends',
        
            

        ] 