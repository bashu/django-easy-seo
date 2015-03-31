# -*- coding: utf-8 -*-

from django import forms

from .models import Seo


class SeoForm(forms.ModelForm):

    class Meta:
        model = Seo
        fields = ['title', 'description', 'keywords']
        widgets = {
            'title': forms.Textarea(attrs={'cols': 120, 'rows': 2}),
            'description': forms.Textarea(attrs={'cols': 120, 'rows': 2}),
            'keywords': forms.Textarea(attrs={'cols': 120, 'rows': 5}),
        }

