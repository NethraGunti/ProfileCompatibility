from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import Profile, Choices, CHOICES


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'status']
    
    def save(self, user, commit=True):
        instance = super(ProfileForm, self).save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance



class Choice1Form(forms.Form):
    option = forms.ChoiceField(choices = [])

    def __init__(self, *args, **kwargs):
        super(Choice1Form, self).__init__(*args, **kwargs)
        if 'choices' in args[0].keys():
            self.fields['option'].choices = args[0]['choices']
                
    def is_valid(self):
        valid = super(Choice1Form, self).is_valid()
        return True
        