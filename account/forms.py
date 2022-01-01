from django import forms
from django.forms.widgets import EmailInput, FileInput, PasswordInput, TextInput, Textarea
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,get_user_model
from account.models import CustomUser

User = get_user_model()
class Loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField( widget=forms.PasswordInput)
    
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
        return super(Loginform, self).clean(*args, **kwargs)  






class RegistertionForm(forms.Form):
    
    
    
    fullname = forms.CharField(widget=TextInput(attrs={ 'class': 'validate form-control', 'placeholder': 'Full Name', 'type': 'text', 'id': 'first_name'}), min_length=2, max_length=150)
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate form-control', 'placeholder': 'Username', 'type': 'text',  'id': 'username'}), min_length=4, max_length=150)
    email = forms.CharField(widget=EmailInput(attrs={'class': 'validate form-control', 'type': 'email', 'placeholder': 'Enter your email address', 'id': 'email'}))
    number = forms.CharField(widget=TextInput(attrs={'class': 'validate form-control', 'type': 'number', 'placeholder': 'phone number', 'id': 'number'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'validate form-control', 'type': 'password', 'placeholder': 'Password', 'id': 'password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'validate form-control', 'type': 'password', 'placeholder': 'Confirm-password', 'id': 'password2'}))
    description = forms.CharField(widget=Textarea(attrs={'class': 'validate form-control',  'placeholder': 'Write about yourself', 'id': 'description'}))
    # picture = forms.CharField(widget=FileInput(attrs={'class': 'validate form-control', 'type': 'file', 'id': 'profile', 'name': 'profile'}))
    
    
    
    # def clean_fullname(self):
    #     fullname = self.cleaned_data['fullname'].lower()
    #     qs = User.objects.filter(fullname=fullname)
    #     if qs.count():
    #         raise forms.ValidationError("Name already exists")
    #     return fullname
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        qp = User.objects.filter(username=username)
        if qp.count():
            raise forms.ValidationError("Username already exist")
        return username
    
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  forms.ValidationError("Email already exists")
        return email
    
    def clean_number(self):
        number = self.cleaned_data['number'].lower()
        r = User.objects.filter(number=number)
        if r.count():
            raise  forms.ValidationError("Phone number already exists")
        return number

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("Password don't match")

        return password2
    
    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            # fullname=self.cleaned_data['fullname'],
            number=self.cleaned_data['number'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            description=self.cleaned_data['description'],
        )
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'photo', 
            'number', 
            'description', 
            'fullname', 
            'about',
            'level',
            'gender',
            ]
        
        

    

 
    
    
    
    