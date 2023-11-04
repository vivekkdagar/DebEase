# This will fix the CD-Rom error that occurs when first using apt on Debian
cat ../../resources/sources.list > /etc/apt/sources.list

# Installing puppet
apt install puppet-master puppet-agent -y

# 
