import subprocess as spr

# Installing gdm3
def gdm_installer():
    command = "sudo apt install gdm3"
    try:
        spr.run(command, shell=True, check=True)
        print("gdm3 installed successfully.")
    except spr.CalledProcessError as e:
        print(f"Error: {e}")

# Installing KDE-Connect
def kde_connect():
    command = "sudo apt install kdeconnect"
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