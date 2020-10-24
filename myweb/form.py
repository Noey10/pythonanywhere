
from django.forms import ModelForm

# ---ใช้สำหรับหน้าสมัคร ---
from django import forms

#---------------------


from .models import Cactus

class Order(ModelForm):
    class Meta:
        model = Cactus
        fields = ['cactusName','cactusPrice', 'amout']

searchchoices = (
        ('lithops bromfieldii', 'lithops bromfieldii'),
        ('echinocereus triglochidiatus', 'ehinocereus triglochidiatus'),
        ('gibbaeum heathii', 'gibbaeum heathii'),
        ('mammillaria johnstonii', 'mammillaria johnstonii'),
        ('mammillaria hubertmulleri', 'mammillaria hubertmulleri'),
        ('weingartia riograndensis', 'weingartia riograndensis'),
        ('weingartia longigibba', 'weingartia longigibba'),
        ('weingartia kargliana', 'weingartia kargliana'),
        ('weingartia trollii', 'weingartia trollii'),
        ('escobaria chihuahuensis', 'escobaria chihuahuensis'),
        ('escobaria laredoi', 'escobaria laredoi'),
        ('escobaria nellieae(minimal)' , 'Escobaria nellieae(minimal)'),
        ('neoporteria subgibbosa', 'neoporteria subgibbosa'),
        ('opuntia phaeacantha', 'opuntia phaeacantha'),
        ('mammillaria goldii', 'mammillaria goldii'),
        ('notocactus ottonis', 'notocactus ottonis'),
        ('ferocactus flavovirens', 'ferocactus flavovirens'),
        ('conophytum calculus', 'conophytum calculus'),
        ('lithops amicorum', 'lithops amicorum'),
        ('gymnocalycium catamarcense', 'gymnocalycium catamarcense'),
        ('lithops aucampiae', 'lithops aucampiae'),
        ('notocactus herteri', 'notocactus herteri'),
        ('notocactus scopa', 'notocactus scopa'),
        ('notocactus uebelmannianus', 'notocactus uebelmannianus'),
        ('conophytum friedrichiae', 'conophytum friedrichiae'),
        ('conophytum subfenestratum', 'conophytum subfenestratum'),
        ('conophytum friedrichiae', 'conophytum friedrichiae'),
        ('opuntia quimilo', 'opuntia quimilo'),
        ('gammillaria gasterantha', 'gammillaria gasterantha'),
        ('gymnocalycium baldianum', 'gymnocalycium baldianum'),

    )

class showOrders(forms.Form):

    cactusName = forms.ChoiceField(choices=searchchoices)
    addamount = forms.CharField(max_length=100)