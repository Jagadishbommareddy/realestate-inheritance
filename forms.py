from django import forms
from .models import Person
from .models import ContactInfo


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = '__all__'

