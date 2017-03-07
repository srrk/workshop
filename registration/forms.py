from django import forms
from django.forms.widgets import RadioSelect
import datetime

class RegForm(forms.Form):
    your_good_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    date_of_birth = forms.DateField(initial=datetime.date.today, error_messages={'invalid': 'Valid format : YYYY-MM-DD'})
    group_choice=[("session-1","morning"),("session-2","post-lunch")]
    radio_choices=[['Modelling', 'md'], ['Sequence', 'seq']]
    group = forms.ChoiceField(widget=RadioSelect(), choices=radio_choices)
    session_id = forms.ChoiceField(group_choice)
