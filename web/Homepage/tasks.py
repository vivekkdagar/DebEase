import subprocess as spr

# Installing gdm3
def gdm_installer():
    command = "sudo apt install gdm3 -y"
    try:
        spr.run(command, shell=True, check=True)
        print("gdm3 installed successfully.")
    except spr.CalledProcessError as e:
        print(f"Error: {e}")

# Installing KDE-Connect
def kde_connect():
    command = "sudo apt install kdeconnect -y"
    try:
        spr.run(command, shell=True, check=True)
        print("KDEConnect installed successfully.")
    except spr.CalledProcessError as e:
        print(f"Error: {e}")

# Installing Linux Mint's WebApp Manager
def mint_webapp():
    command = "sudo dpkg -i ../resources/web*"
    try:
        spr.run(command, shell=True, check=True)
        print("WebApp Manager installed successfully.")
    except spr.CalledProcessError as e:
        print(f"Error: {e}")
        
# Customize terminal
def theme_terminal():
    command = "sudo bash ../cli/Customization/terminal-theme.sh"
    try:
        spr.run(command, shell=True, check=True)
        print("gdm3 installed successfully.")
    except spr.CalledProcessError as e:
        print(f"Error: {e}")

# CPU Firmware (Microcode)
def cpu_firmware():
    command = "sudo bash ../cli/Recommended/drivers/cpu-drivers.sh"
    try:
        spr.run(command, shell=True, check=True)
        print("Microcode installed successfully")
    except spr.CalledProcessError as e:
        print(f"Error: {e}")

# GPU Drivers
def gpu_driv():
    command="sudo bash ../cli/Recommended/drivers/gpu-drivers.sh"
    try:
        spr.run(command, shell=True, check=True)
        print("Microcode installed successfully")
    except spr.CalledProcessError as e:
        print(f"Error: {e}")

# Install nala and make it the default package manager
def nala_pkg():
    command="sudo bash ../cli/Recommended/apt-nala.sh"
    try:
        spr.run(command, shell=True, check=True)
        print("nala installed successfully")
    except spr.CalledProcessError as e:
        print(f"Error: {e}")
        
# Setup tlp battery saver
def setup_tlp():
    command="sudo bash ../cli/Recommended/battery-saver.sh"
    try:
        spr.run(command, shell=True, check=True)
        print("Battery saver installed successfully")
    except spr.CalledProcessError as e:
        print(f"Error: {e}")
        
# Installing KDE-Connect
def timeshift():
    command = "sudo apt install timeshift -y"
    try:
        spr.run(command, shell=True, check=True)
        print("KDEConnect installed successfully.")
    except spr.CalledProcessError as e:
        print(f"Error: {e}")
        
# Setup ufw firewall
def setup_ufw():
    command="sudo bash ../cli/Recommended/ufw-firewall.sh"
    try:
        spr.run(command, shell=True, check=True)
        print("Battery saver installed successfully")
    except spr.CalledProcessError as e:
        print(f"Error: {e}")

def setup_ulauncher():
    command="sudo bash ../cli/Recommended/setup-ulauncher.sh"
    try:
        spr.run(command, shell=True, check=True)
        print("appLauncher installed successfully")
    except spr.CalledProcessError as e:
        print(f"Error: {e}")