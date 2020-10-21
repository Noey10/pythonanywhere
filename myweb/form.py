from django.db.models import fields
from django.forms import ModelForm

# ---ใช้สำหรับหน้าสมัคร ---
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#---------------------


from .models import Cactus, MyUser

class Order(ModelForm):
    class Meta:
        model = Cactus
        fields = ['cactusName','cactusPrice', 'amout']


class addUsers(ModelForm):

    class Meta:
        model = MyUser
        fields = ["Firstname","Lastname","username","password","email"]


searchchoices = (
        (1 , 'Echinocereus triglochidiatus'),
        (2 , 'Gibbaeum heathii'),
        (3 , 'test'),
        (4 , 'test2'),

    )

class showOrders(forms.Form):

    cactusName = forms.ChoiceField(choices=searchchoices)
    addamount = forms.CharField(max_length=100)