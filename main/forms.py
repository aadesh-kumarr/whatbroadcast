from django import forms 
import datetime
# from django_countries.fields import CountryField

class logdat(forms.Form):
    username=forms.CharField(label='username',max_length=20,required=True)
    fname=forms.CharField(label='first name',max_length=20,required=True)
    lname=forms.CharField(label='last name',max_length=20,required=True)
    email=forms.EmailField(label="email",max_length=254,required=True)
    password=forms.CharField(label="password",widget=forms.PasswordInput(),required=True)
     

class login_page(forms.Form):
    email=forms.EmailField(label="email",max_length=254, required=True)
    password=forms.CharField(label="password",widget=forms.PasswordInput(),required=True)
    
class msg(forms.Form):
    txt=forms.CharField(label='Enter the message to be sent',max_length=1000, required=True, widget=forms.DateInput)
    image=forms.ImageField(label='please select the image', required=True)
    excelfile=forms.FileField(label='please select the excel file containing names/numbers', required=True)
    
    # speed=forms.MultipleChoiceField(choices={'slow','medium','fast'})
