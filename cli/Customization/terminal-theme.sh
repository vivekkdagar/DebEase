# Nerd Font
curl -sS https://webi.sh/nerdfont | sh

# Update envman
source ~/.config/envman/PATH.env

# Installing starship
curl -sS https://starship.rs/install.sh | sh

# Attach it to shell
echo 'eval "$(starship init bash)"' >> ~/.bashrc

# Pure Preset for starship
starship preset pure-preset -o ~/.config/starship.toml

