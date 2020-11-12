# -*- coding: utf-8 -*-
from decimal import Decimal

from django import forms
from django.core.validators import MinValueValidator

from loans.models import Client


class ClientForm(forms.ModelForm):
    """Client form. """
    GENDER = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )

    du = forms.IntegerField(label='DU', max_value=99000000, required=True, widget=forms.TextInput(attrs={'placeholder': '99999999'}))
    name = forms.CharField(label='Name', max_length=30, required=True)
    surname = forms.CharField(label='Last Name', max_length=30, required=True)
    gender = forms.ChoiceField(label='Gender', required=True, choices=GENDER, widget=forms.Select(attrs={'class': 'form-group'}))
    email = forms.EmailField(label='Email', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'name@domain.com'}))
    total = forms.FloatField(label='Total', max_value=100000, initial=1000.00, validators=[MinValueValidator(Decimal('0.00'))])

    class Meta:
        model = Client
        exclude = []
