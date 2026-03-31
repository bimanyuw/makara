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
                ('Plus Jakarta Sans', 'Plus Jakarta Sans (Modern)'),
                ('Georgia', 'Georgia (Serif Klasik)'),
                ('Verdana', 'Verdana (Sans-serif Bersih)'),
                ('Tahoma', 'Tahoma (Kompak)'),
                ('Times New Roman', 'Times New Roman (Formal)'),
                ('Courier New', 'Courier New (Monospace)'),
            ]),
            'site_title': forms.TextInput(attrs={'placeholder': 'MAKARA'}),
        }