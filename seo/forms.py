# -*- coding: utf-8 -*-

from django import forms

from .models import Seo


class SeoForm(forms.ModelForm):

    class Meta:
        model = Seo
        fields = ['title', 'description', 'keywords']

    def __init__(self, *args, **kwargs):
        super(SeoForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget = forms.Textarea(
            attrs={'cols': '120', 'rows': '2'})

        self.fields['description'].widget = forms.Textarea(
            attrs={'cols': '120', 'rows': '2'})

        self.fields['keywords'].widget = forms.Textarea(
            attrs={'cols': '120', 'rows': '5'})
