sudo nala install tlp tlp-rdw
sudo tlp start
sudo nala install python3-gi git python3-setuptools python3-stdeb dh-python
git clone https://github.com/d4nj1/TLPUI
cd TLPUI
python3 setup.py --command-packages=stdeb.command bdist_deb
sudo dpkg -i deb_dist/python3-tlpui_*all.deb