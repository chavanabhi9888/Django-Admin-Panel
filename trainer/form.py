from dataclasses import field
from django import forms
from trainer.models import trainer

class Enquiry(forms.ModelForm):
    class Meta:
        model = trainer
        fields = '__all__'