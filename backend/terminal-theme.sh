sudo apt install curl wget build-essential -y

# Install envman
curl -sS https://webi.sh/nerdfont | sh

# Source bashrc
source ~/.bashrc

# Install starship
curl -sS https://starship.rs/install.sh | sh

# Add it to bashrc
eval "$(starship init bash)"

# Apply starship theme
starship preset no-nerd-font -o ~/.config/starship.toml