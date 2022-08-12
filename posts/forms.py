from django import forms
from .models import Message
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


import django
django.setup()
from users.models import User


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('sender', 'receiver',)
        
class BirthdayPageForm(forms.ModelForm):
    CAKE_CHOICES = [
        ("초코 케이크", "초코"),
        ("딸기 케이크", "딸기"),
        ("치즈 케이크", "치즈"),
    ]
    selected_cake = forms.ChoiceField(choices=CAKE_CHOICES, widget=forms.RadioSelect)
    birthday = forms.DateField(
        widget=forms.SelectDateWidget(empty_label=('Year', 'Month', 'Day'))
        )
    class Meta:
        model = User
        fields = ('full_name', 'birthday', 'selected_cake')
        