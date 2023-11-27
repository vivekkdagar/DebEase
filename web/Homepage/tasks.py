import subprocess as spr

def execute(command):
    try:
        spr.run(command, shell=True, check=True)
    except spr.CalledProcessError as e:
        print(f"Error: {e} occured in {command}")

# Installing KDE-Connect
def kde_connect():
    execute("sudo apt install kdeconnect -y")
    print("KDE-Connect installed successfully.")

# Installing gdm3
def gdm_installer():
    execute("sudo apt install gdm3 -y")
    print("gdm3 installed successfully.")

# Installing timeshift
def timeshift():
    execute("sudo apt install timeshift -y")
    print("Timeshift installed successfully.")

# Installing Linux Mint's webapp manager
def mint_webapp():
    execute("sudo dpkg -i ../resources/webapp*")
    print("WebApp Manager installed successfully.")

# Customize terminal
def theme_terminal():
    execute("sudo apt install curl wget build-essential -y")
    execute("curl -sS https://webi.sh/nerdfont | sh")
    execute("source ~/.bashrc")
    execute("curl -sS https://starship.rs/install.sh | sh")
    init_starship = 'eval "$(starship init bash)"'
    execute(f"sudo echo {init_starship} >> ~/.bashrc")
    execute("starship preset no-nerd-font -o ~/.config/starship.toml")
    print("Terminal customized successfully.")

# CPU Firmware (Microcode)
def cpu_firmware():
    execute("sudo bash ../backend/cpu-drivers.sh")
    print("Microcode installed successfully.")
    
# GPU Drivers
def gpu_driv():
    execute("sudo bash ../backend/gpu-drivers.sh")
    print("GPU Drivers installed successfully.")
    
# Install nala and make it the default package manager
def nala_pkg():
    execute("sudo apt install nala -y")
    execute("sudo cat ../resources/nala* >> ~/.bashrc")
    print("nala installed successfully.")

# Setup tlp battery saver
def setup_tlp():
    execute("sudo bash ../backend/battery-saver.sh")
    print("Battery saver installed successfully.")
    
# Setup ufw firewall
def setup_ufw():
    execute("sudo bash ../backend/ufw-firewall.sh")
    print("Firewall is up and running now.")

# Install and setup ulauncher
def setup_ulauncher():
    execute("sudo bash ../backend/setup-ulauncher.sh")
    print("appLauncher installed successfully.")

# Setup terminal aliases
def aliases():
    execute("sudo bash ../backend/setup-aliases.sh")
    print("Terminal aliases set successfully.")

# Cusstomize nemo file manager
def nemo():
    execute("sudo bash ../backend/setup-nemo.sh")
    print("Nemo file manager setup successfully.")

# Set custom scripts
def custom_scripts():
    execute("sudo bash ../backend/custom-scrpts.sh")
    print("Custom scripts are located at ~/Documents/.")

# Theme libreoffice
def libre_office():
    execute("sudo bash ../backend/libre-office.sh")
    print("Setup libreoffice done successfully.")