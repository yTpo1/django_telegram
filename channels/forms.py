from django import forms
from .models import Channel


class AddChannelForm(forms.ModelForm):
    channel_username = forms.CharField(widget=forms.HiddenInput, label='')

    class Meta:
        model = Channel
        fields = ['channel_username', 'description', 'category', 'language']

