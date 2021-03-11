from django import forms
from Applicationuser.models import Application_user,Hotel
class ApplicationuserForm(forms.ModelForm):
    class Meta():
        model = Application_user
        exclude = ['first_name', 'last_name', 'email',
                   'password', 'phone_no', 'city', 'address', 'otp', 'otp_gen_time'
                   'user_type', 'token', 'user_image']


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']
