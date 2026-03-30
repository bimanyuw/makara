from django import forms
from .models import SiteAppearance


class AppearanceForm(forms.ModelForm):
    class Meta:
        model = SiteAppearance
        fields = ['site_title', 'primary_color', 'background_color', 'font_family']
        widgets = {
            'primary_color': forms.TextInput(attrs={'type': 'color'}),
            'background_color': forms.TextInput(attrs={'type': 'color'}),
            'font_family': forms.Select(choices=[
                ('Arial', 'Arial'),
                ('Georgia', 'Georgia'),
                ('Tahoma', 'Tahoma'),
                ('Verdana', 'Verdana'),
                ('Times New Roman', 'Times New Roman'),
            ])
        }