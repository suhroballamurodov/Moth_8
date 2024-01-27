from django import forms
from .models import UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name','last_name', 'email', 'subyekt','message']



# ''' Bu ikkinchi yo'l '''
# class UserForm(forms.Form):
#     name = forms.CharField(label='Ismingiz')
#     last_name = forms.CharField(label='Familiyasi')
#     email = forms.EmailField(label='Email manzilingiz')
#     subyekt = forms.CharField(label='Xabarni qisqacha mazmuni', widget=forms.Textarea)
#     message = forms.CharField(label='Xabaringiz', widget=forms.Textarea)
    

