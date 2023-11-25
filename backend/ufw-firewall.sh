nala install ufw

# Source for these rules is Chris Titus Tech.
sudo ufw limit 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 80/tcp
sudo ufw default deny incoming
sudo ufw default allow outgoing

sudo ufw enable