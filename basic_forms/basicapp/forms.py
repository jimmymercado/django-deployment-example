from django import forms
from django.core import validators


#custom made validation:
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name must begin win Z')

class FormName(forms.Form):
    name = forms.CharField(label='Full Name', validators=[check_for_z])
    email = forms.EmailField(label='Email Address', initial='name@domain.com')
    verify_email = forms.EmailField(label='Enter Email Again')
    text = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)]) 
   
    #validator using the function within class
    '''
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('Gotcha bot!')

        return botcatcher
    '''

    #clean data all at once
    def clean(self):
        all_clean = super().clean()
        email = all_clean['email']
        vemail = all_clean['verify_email']

        if email != vemail:
            raise forms.ValidationError('Email does not match!')