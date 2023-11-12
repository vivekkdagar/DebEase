# This will fix the CD-Rom error that occurs when first using apt on Debian
cat ./resources/dependencies/sources.list > /etc/apt/sources.list

# Installing puppet
apt install puppet puppet-master build-essential puppet-agent -y

# Installing packages
sudo puppet apply ./resources/dependencies/packages.pp

# Update system
sudo apt update && sudo apt upgrade
