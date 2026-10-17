from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
   email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm'}))

   class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']

   def init(self, args, **kwargs):
       super(UserRegistrationForm, self).init(args, **kwargs)
       for fieldname in ['username', 'password1', 'password2']:
           self.fields[fieldname].widget.attrs['class'] = 'form-control form-control-sm'