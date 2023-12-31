# Homepage/forms.py
from django import forms

class RunForm(forms.Form):
    login_manager = forms.BooleanField(
        required=False,
        initial=False,
    )
    
    kde = forms.BooleanField(
        required=False,
        initial=False,
    )
    
    web_apps = forms.BooleanField(
        required=False,
        initial=False,
    )
    
    terminal_starship = forms.BooleanField(
        required=False,
        initial=False,
    )
    
    cpu_drivers = forms.BooleanField(
        required=False,
        initial=False,
    )
    
    gpu_drivers = forms.BooleanField(
        required=False,
        initial=False,
    )
    
    nala_install = forms.BooleanField(
        required=False,
        initial=False,
    )
    
    battery_saver = forms.BooleanField(
        required=False,
        initial=False,
    )
    
    ulauncher = forms.BooleanField(
        required=False,
        initial=False,
    )
    
    firewall = forms.BooleanField(
        required=False,
        initial=False,
    )
    
    backup = forms.BooleanField(
        required=False,
        initial=False,
    )
    
    custom_scrps = forms.BooleanField(
        required=False,
        initial=False,
    )
    
    aliases = forms.BooleanField(
        required=False,
        initial=False,
    )    
    
    libreoffice_theme = forms.BooleanField(
        required=False,
        initial=False,
    )

