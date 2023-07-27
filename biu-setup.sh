#!/bin/bash
#install gh desktop
wget -qO - https://apt.packages.shiftkey.dev/gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/shiftkey-packages.gpg > /dev/null
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/shiftkey-packages.gpg] https://apt.packages.shiftkey.dev/ubuntu/ any main" > /etc/apt/sources.list.d/shiftkey-packages.list'
# Install other useful packages 
sudo apt install neovim python3-pip 
#Install python libraries with pip
pip3 install guizero
#login to github CLI
#setup raspberry pi for eduroam
cd ~/Desktop/
gh repo clone Liam-Twomey/RaspberryPi_Eduroam
gh repo clone Liam-Twomey/BIUcontrol
gh repo clone Liam-Twomey/BIUcontrol-pulse
