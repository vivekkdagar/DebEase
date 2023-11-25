from django.shortcuts import render
from .forms import RunForm
from .tasks import *

def run_page(request):
    if(request.method == "POST"):
        form = RunForm(request.POST)
        if form.is_valid():
            selected_options = form.cleaned_data
            if selected_options["login_manager"]:
            # Installing gdm3 to be the default login manager
              gdm_installer()
            if selected_options["kde"]:
              kde_connect()
            if selected_options["web_apps"]:
              mint_webapp()
            if selected_options["terminal_starship"]:
                theme_terminal()
            if selected_options["cpu_drivers"]:
                cpu_firmware()
            if selected_options["gpu_drivers"]:
                gpu_driv()
            if selected_options["nala_install"]:
                nala_pkg()
    else:
        form = RunForm()
    return render(request, "index.html", {'form': form})

