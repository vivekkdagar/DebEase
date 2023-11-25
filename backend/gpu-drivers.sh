#!/bin/bash

read -p "Do you have an NVIDIA GPU? (N/n) or an AMD GPU? (A/a): " choice

if [ "$choice" == "N" ] || [ "$choice" == "n" ]; then
  # If the user has an NVIDIA GPU, execute these commands
  sudo apt install nvidia-detect -y
  sudo nvidia-detect
  sudo apt install nvidia-driver -y
elif [ "$choice" == "A" ] || [ "$choice" == "a" ]; then
  # If the user has an AMD GPU, execute these commands
  sudo apt install firmware-linux firmware-linux-nonfree libdrm-amdgpu1 xserver-xorg-video-amdgpu -y
else
  echo "Invalid choice. Please enter 'N' or 'A' to indicate your GPU type."
fi
