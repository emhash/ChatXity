from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Profile


class CommonRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email','username','password1', 'password2']
        

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
    
        if not email:
            raise forms.ValidationError("Please provide either email or username.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Enter your email address'})
        self.fields['email'].label = 'Email'

        self.fields['username'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Enter a unique username'})
        self.fields['username'].label = 'Username'

        self.fields['password1'].widget.attrs.update({'class': 'form-control mb-2 fakepassword', 'id':'psw-input', 'placeholder': 'Set password'})
        self.fields['password1'].label = 'Password'

        self.fields['password2'].widget.attrs.update({'class': 'form-control mb-2 fakepassword', 'placeholder': 'Confirm your password'})
        self.fields['password2'].label = 'Confirm Password'



# class AddUserByAdminForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['email', 'password1', 'password2','role','user_permissions', ]
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
#                 if field == 'user_permissions':
#                     self.fields[field].widget.attrs.update({'class': 'form-control', 'style':"height:250px;"})
#                 else:
#                     self.fields[field].widget.attrs.update({'class': 'form-control',})
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user', 'fill_up', 'registered']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["first_name"].widget.attrs.update(
            {'class': 'form-control mb-2', 
                
            }
            
            )
        self.fields["last_name"].widget.attrs.update(
            {'class': 'form-control mb-2', 
                
            }
            
            )
        self.fields["phone_number"].widget.attrs.update(
            {'class': 'form-control mb-2', 
                
            }
            
            )
        self.fields["gender"].widget.attrs.update(
            {'class': 'form-control mb-2', 
                
            }
            
            )
        self.fields["birthday"].widget.attrs.update(
            {'class': 'form-control mb-2 flatpickr flatpickr-input', 
                
            }
            
            )
        self.fields["profile_picture"].widget.attrs.update(
            {'class': 'form-control mb-2', 
                
            }
            
            )
        self.fields["bio"].widget.attrs.update(
            {'class': 'form-control mb-2 pb-4',
             
            #  'style':"height:150px;"
            }
            
            )
        