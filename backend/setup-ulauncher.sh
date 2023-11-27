# Download and install
wget https://github.com/Ulauncher/Ulauncher/releases/download/5.15.3/ulauncher_5.15.3_all.deb
chmod +x ulau*
apt install ./ulau*
rm ulau*

# Configuration
rm ~/.config/ulauncher
cp -r ../resources/ulauncher ~/.config/ulauncher
